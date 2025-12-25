import streamlit as st
from analyse_frequences import analyser_frequences
from construction_arbre import construire_arbre
from encodage import generer_codes, encoder
from decodage import calculer_stats
import graphviz

st.set_page_config(page_title="Huffman Visualizer", layout="wide")

st.title(" Codage de Huffman – Visualisation & Animation")

fichier = st.file_uploader(" Importer un fichier texte", type=["txt"])

if fichier:
    texte = fichier.read().decode("utf-8")

    # Affichage du texte original
    st.subheader("Texte original")
    with st.expander("Voir le texte", expanded=False):
        st.text(texte)
    
    st.info(f"Longueur du texte : {len(texte)} caractères")

    # Analyse des fréquences
    st.subheader("Analyse des fréquences")
    frequences = analyser_frequences(texte)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("**Tableau des fréquences:**")
        freq_sorted = sorted(frequences.items(), key=lambda x: x[1], reverse=True)
        for char, freq in freq_sorted[:10]:
            char_display = repr(char) if char in ['\n', '\t', ' '] else char
            st.write(f"`{char_display}` : {freq}")
        if len(freq_sorted) > 10:
            st.write(f"... et {len(freq_sorted) - 10} autres caractères")
    
    with col2:
        st.bar_chart({char: freq for char, freq in freq_sorted[:15]})

    # Construction de l'arbre
    st.subheader(" Arbre de Huffman")
    arbre = construire_arbre(frequences)
    
    # Fonction pour créer la visualisation Graphviz
    def visualiser_arbre(noeud, graph=None, parent=None, edge_label="", node_id=0):
        if graph is None:
            graph = graphviz.Digraph(comment='Arbre de Huffman')
            graph.attr(rankdir='TB')
            graph.attr('node', shape='circle', style='filled', fontname='Arial')
        
        current_id = str(node_id[0])
        node_id[0] += 1
        
        # Vérifier si c'est une feuille (caractère)
        if hasattr(noeud, 'char') and noeud.char is not None:
            char_display = repr(noeud.char) if noeud.char in ['\n', '\t', ' '] else noeud.char
            label = f"{char_display}\n({noeud.freq})"
            graph.node(current_id, label, fillcolor='lightblue', fontsize='12')
        else:
            # Noeud interne
            label = f"{noeud.freq}"
            graph.node(current_id, label, fillcolor='lightgray', fontsize='12')
        
        # Ajouter l'arête depuis le parent
        if parent is not None:
            graph.edge(parent, current_id, label=edge_label, fontsize='10', color='red' if edge_label == '0' else 'green')
        
        # Parcourir les enfants
        if hasattr(noeud, 'gauche') and noeud.gauche:
            visualiser_arbre(noeud.gauche, graph, current_id, '0', node_id)
        if hasattr(noeud, 'droite') and noeud.droite:
            visualiser_arbre(noeud.droite, graph, current_id, '1', node_id)
        
        return graph
    
    # Créer et afficher le graphe
    node_counter = [0]
    graph = visualiser_arbre(arbre, node_id=node_counter)
    st.graphviz_chart(graph)
    
    st.info("Arête rouge = bit '0' | Arête verte = bit '1'")

    # Génération des codes
    st.subheader(" Codes de Huffman")
    codes = generer_codes(arbre)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Table des codes:**")
        codes_sorted = sorted(codes.items(), key=lambda x: len(x[1]))
        for char, code in codes_sorted[:15]:
            char_display = repr(char) if char in ['\n', '\t', ' '] else char
            st.code(f"{char_display} → {code}")
        if len(codes_sorted) > 15:
            st.write(f"... et {len(codes_sorted) - 15} autres codes")
    
    with col2:
        st.write("**Statistiques des codes:**")
        code_lengths = [len(code) for code in codes.values()]
        st.write(f"Longueur minimale : {min(code_lengths)} bits")
        st.write(f"Longueur maximale : {max(code_lengths)} bits")
        st.write(f"Longueur moyenne : {sum(code_lengths)/len(code_lengths):.2f} bits")

    # Encodage
    st.subheader("Encodage")
    texte_encode = encoder(texte, codes)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Taille originale", f"{len(texte) * 8} bits")
    with col2:
        st.metric("Taille encodée", f"{len(texte_encode)} bits")
    
    taux_compression = (1 - len(texte_encode) / (len(texte) * 8)) * 100
    st.success(f"Taux de compression : {taux_compression:.2f}%")
    
    with st.expander("Voir le texte encodé (premiers 500 bits)"):
        st.code(texte_encode[:500] + ("..." if len(texte_encode) > 500 else ""))

else:
    st.info(" Veuillez importer un fichier texte pour commencer l'analyse")
    
    # Exemple de démonstration
    with st.expander("Voir un exemple"):
        st.write("""
        **Comment fonctionne l'algorithme de Huffman ?**
        
        1. **Analyse des fréquences** : Compte l'occurrence de chaque caractère
        2. **Construction de l'arbre** : Crée un arbre binaire optimal basé sur les fréquences
        3. **Génération des codes** : Assigne des codes binaires courts aux caractères fréquents
        4. **Encodage** : Remplace chaque caractère par son code de Huffman
        
        Les caractères les plus fréquents reçoivent les codes les plus courts !
        """)