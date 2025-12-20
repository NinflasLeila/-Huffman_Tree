"""
Module d'analyse des fréquences pour l'algorithme de Huffman
Auteur: Personne 1
Description: Lecture d'un fichier texte et comptage des fréquences de caractères
"""

class Noeud:
    """
    Représente un nœud de l'arbre de Huffman
    
    Attributs:
        caractere (str): Le caractère stocké (None pour les nœuds internes)
        frequence (int): La fréquence d'apparition du caractère
        gauche (Noeud): Le fils gauche (None si feuille)
        droit (Noeud): Le fils droit (None si feuille)
    """
    def __init__(self, caractere=None, frequence=0, gauche=None, droit=None):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = gauche
        self.droit = droit
    
    def est_feuille(self):
        """Vérifie si le nœud est une feuille (pas d'enfants)"""
        return self.gauche is None and self.droit is None
    
    def __repr__(self):
        """Représentation pour le débogage"""
        if self.caractere:
            return f"Noeud('{self.caractere}', freq={self.frequence})"
        return f"Noeud(freq={self.frequence})"
    
    def __lt__(self, autre):
        """Comparaison pour le tri (nécessaire pour heapq)"""
        return self.frequence < autre.frequence


def lire_fichier(chemin_fichier):
    """
    Lit le contenu d'un fichier texte
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier à lire
        
    Returns:
        str: Le contenu du fichier
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        UnicodeDecodeError: Si le fichier n'est pas en UTF-8
    """
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(f"Erreur d'encodage lors de la lecture du fichier '{chemin_fichier}'.")


def calculer_frequences(texte):
    """
    Calcule la fréquence d'apparition de chaque caractère dans le texte
    
    Args:
        texte (str): Le texte à analyser
        
    Returns:
        dict: Dictionnaire {caractère: fréquence}
        
    Exemple:
        >>> calculer_frequences("aabbc")
        {'a': 2, 'b': 2, 'c': 1}
    """
    frequences = {}
    
    for caractere in texte:
        if caractere in frequences:
            frequences[caractere] += 1
        else:
            frequences[caractere] = 1
    
    return frequences


def creer_noeuds_feuilles(frequences):
    """
    Crée une liste de nœuds feuilles à partir du dictionnaire de fréquences
    
    Args:
        frequences (dict): Dictionnaire {caractère: fréquence}
        
    Returns:
        list: Liste de Noeud (feuilles de l'arbre)
    """
    noeuds = []
    
    for caractere, frequence in frequences.items():
        noeud = Noeud(caractere=caractere, frequence=frequence)
        noeuds.append(noeud)
    
    return noeuds


def afficher_frequences(frequences, trier=True):
    """
    Affiche les fréquences de manière lisible
    
    Args:
        frequences (dict): Dictionnaire {caractère: fréquence}
        trier (bool): Si True, trie par fréquence décroissante
    """
    print("\n" + "="*50)
    print("ANALYSE DES FRÉQUENCES")
    print("="*50)
    
    # Trier si demandé
    if trier:
        items = sorted(frequences.items(), key=lambda x: x[1], reverse=True)
    else:
        items = frequences.items()
    
    print(f"\nNombre de caractères uniques : {len(frequences)}")
    print(f"Nombre total de caractères : {sum(frequences.values())}\n")
    
    print(f"{'Caractère':<15} {'Fréquence':<10} {'Pourcentage'}")
    print("-"*50)
    
    total = sum(frequences.values())
    
    for caractere, freq in items:
        # Affichage spécial pour les caractères non imprimables
        if caractere == ' ':
            affichage = '[ESPACE]'
        elif caractere == '\n':
            affichage = '[RETOUR]'
        elif caractere == '\t':
            affichage = '[TAB]'
        else:
            affichage = caractere
        
        pourcentage = (freq / total) * 100
        print(f"{affichage:<15} {freq:<10} {pourcentage:>6.2f}%")
    
    print("="*50 + "\n")


def analyser_fichier(chemin_fichier):
    """
    Fonction principale qui analyse un fichier et retourne les structures nécessaires
    
    Args:
        chemin_fichier (str): Le chemin vers le fichier à analyser
        
    Returns:
        tuple: (texte, frequences, noeuds_feuilles)
    """
    print(f"Lecture du fichier : {chemin_fichier}")
    texte = lire_fichier(chemin_fichier)
    
    print("Calcul des fréquences...")
    frequences = calculer_frequences(texte)
    
    print("Création des nœuds feuilles...")
    noeuds = creer_noeuds_feuilles(frequences)
    
    return texte, frequences, noeuds


# ==================== TESTS UNITAIRES ====================

def test_calculer_frequences():
    """Test de la fonction calculer_frequences"""
    print("\n🧪 Test : calculer_frequences")
    
    # Test 1
    resultat = calculer_frequences("aabbc")
    attendu = {'a': 2, 'b': 2, 'c': 1}
    assert resultat == attendu, f"Échec : attendu {attendu}, obtenu {resultat}"
    print("✅ Test 1 réussi : 'aabbc'")
    
    # Test 2
    resultat = calculer_frequences("hello")
    attendu = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert resultat == attendu, f"Échec : attendu {attendu}, obtenu {resultat}"
    print("✅ Test 2 réussi : 'hello'")
    
    # Test 3 : texte vide
    resultat = calculer_frequences("")
    attendu = {}
    assert resultat == attendu, f"Échec : attendu {attendu}, obtenu {resultat}"
    print("✅ Test 3 réussi : texte vide")
    
    print("✅ Tous les tests de calculer_frequences sont réussis !\n")


def test_creer_noeuds_feuilles():
    """Test de la fonction creer_noeuds_feuilles"""
    print("\n🧪 Test : creer_noeuds_feuilles")
    
    frequences = {'a': 5, 'b': 3}
    noeuds = creer_noeuds_feuilles(frequences)
    
    assert len(noeuds) == 2, f"Échec : attendu 2 nœuds, obtenu {len(noeuds)}"
    assert all(isinstance(n, Noeud) for n in noeuds), "Échec : tous les éléments doivent être des Noeud"
    assert all(n.est_feuille() for n in noeuds), "Échec : tous les nœuds doivent être des feuilles"
    
    print("✅ Tous les tests de creer_noeuds_feuilles sont réussis !\n")


def test_noeud():
    """Test de la classe Noeud"""
    print("\n🧪 Test : Classe Noeud")
    
    # Test création nœud feuille
    noeud1 = Noeud('a', 5)
    assert noeud1.caractere == 'a', "Échec : caractère incorrect"
    assert noeud1.frequence == 5, "Échec : fréquence incorrecte"
    assert noeud1.est_feuille(), "Échec : devrait être une feuille"
    print("✅ Test 1 réussi : création nœud feuille")
    
    # Test création nœud interne
    noeud2 = Noeud('b', 3)
    noeud_parent = Noeud(None, 8, noeud1, noeud2)
    assert not noeud_parent.est_feuille(), "Échec : ne devrait pas être une feuille"
    assert noeud_parent.frequence == 8, "Échec : fréquence incorrecte"
    print("✅ Test 2 réussi : création nœud interne")
    
    # Test comparaison
    assert noeud2 < noeud1, "Échec : comparaison incorrecte"
    print("✅ Test 3 réussi : comparaison de nœuds")
    
    print("✅ Tous les tests de Noeud sont réussis !\n")


def executer_tous_les_tests():
    """Execute tous les tests unitaires"""
    print("\n" + "="*60)
    print("EXÉCUTION DES TESTS UNITAIRES")
    print("="*60)
    
    test_noeud()
    test_calculer_frequences()
    test_creer_noeuds_feuilles()
    
    print("="*60)
    print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
    print("="*60 + "\n")


# ==================== EXEMPLE D'UTILISATION ====================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("MODULE D'ANALYSE DES FRÉQUENCES - HUFFMAN")
    print("="*60 + "\n")
    
    # 1. Exécuter les tests
    executer_tous_les_tests()
    
    # 2. Exemple avec un texte simple
    print("="*60)
    print("EXEMPLE D'UTILISATION")
    print("="*60 + "\n")
    
    texte_exemple = "HOURRA HOURRA HOURRRRA ?"
    print(f"Texte d'exemple : \"{texte_exemple}\"\n")
    
    frequences = calculer_frequences(texte_exemple)
    afficher_frequences(frequences)
    
    noeuds = creer_noeuds_feuilles(frequences)
    print(f"Nombre de nœuds créés : {len(noeuds)}")
    print("\nExemples de nœuds créés :")
    for i, noeud in enumerate(noeuds[:5]):  # Afficher les 5 premiers
        print(f"  {i+1}. {noeud}")
    
    # 3. Test avec un fichier (si disponible)
    print("\n" + "="*60)
    print("TEST AVEC UN FICHIER")
    print("="*60 + "\n")
    
    try:
        texte, frequences, noeuds = analyser_fichier('test.txt')
        afficher_frequences(frequences)
        print(f"\n✅ Fichier analysé avec succès!")
        print(f"   - Taille du texte : {len(texte)} caractères")
        print(f"   - Caractères uniques : {len(frequences)}")
        print(f"   - Nœuds créés : {len(noeuds)}")
    except FileNotFoundError:
        print("⚠️  Fichier 'test.txt' non trouvé.")
        print("   Créez un fichier test.txt dans le même dossier pour tester.")
    
    print("\n" + "="*60)
    print("Pour analyser votre propre fichier, utilisez :")
    print("  texte, frequences, noeuds = analyser_fichier('mon_fichier.txt')")
    print("="*60 + "\n")