
# Encodage Huffman - Partie Siham Tayebi
# Objectif : Générer les codes binaires pour chaque caractère,
#  encoder un texte et sauvegarder le résultat.
# Ce module utilise :
# - l'analyse des fréquences (Personne 1)
# - la construction de l'arbre de Huffman (Personne 2)

# Objectif :
# Transformer l'arbre de Huffman en table de codes binaires,
# puis encoder un texte caractère par caractère.

from analyse_frequences import Noeud,  analyser_fichier , lire_fichier
from construction_arbre import construire_arbre_huffman, afficher_arbre, creer_noeuds_feuilles
from typing import Dict, Optional , List

# -------------------------------
# Étape 1 : Générer la table de codage
# -------------------------------
#  Réccupérer l'arbre de Huffman
def  recuperer_arbre_huffman():
    """
    Construit et retourne l'arbre de Huffman à partir du fichier texte.

    Étapes :
    1. Récupérer uniquement les fréquences depuis analyser_fichier
    2. Créer les nœuds feuilles à partir des fréquences
    3. Construire l'arbre de Huffman final

    Returns:
        Noeud: racine de l'arbre de Huffman
    """
    #  envoyer analyser_fichier("test.txt")  pour obtenir les fréquences
    frequences = analyser_fichier("test.txt")[1]
    #  envoyer creer_noeuds_feuilles ( fréquences ) pour obtenir les feuilles
    # Envoyer construire_arbre_huffman ( feuilles ) pour obtenir la racine de l’arbre
    return  construire_arbre_huffman( creer_noeuds_feuilles( frequences ) )
# Récupèrer l’arbre de Huffman fourni par Personne 2.: Elbatoul hnagnag
def verifier_arbre_huffman(racine: Optional[Noeud]) -> bool:
    """
    Vérifie la validité structurelle de l'arbre de Huffman.

    Conditions :
    - Une feuille contient un caractère et une fréquence > 0
    - Un nœud interne n'a pas de caractère
    - Chaque nœud interne possède deux enfants
    """
    # Cas de base : arbre vide → invalide
    if racine is None:
        return False

    # Si c’est une feuille
    if racine.est_feuille():
        return (
            racine.caractere is not None and
            racine.frequence > 0 and
            racine.gauche is None and
            racine.droit is None
        )

    # Si c’est un nœud interne
    if racine.caractere is None:
        if racine.gauche is None or racine.droit is None:
            return False
        if racine.frequence <= 0:
            return False

        # Vérifier récursivement les deux sous-arbres
        return (
            verifier_arbre_huffman(racine.gauche) and
            verifier_arbre_huffman(racine.droit)
        )

    # Autres cas → invalide
    return False


  
def generer_codes_huffman(racine: Optional[Noeud]) -> Dict[str, str]:
    """
    Génère les codes de Huffman pour chaque caractère en parcourant l'arbre de Huffman.

    Args:
        racine (Noeud | None): Racine de l'arbre de Huffman

    Principe :
        - Aller à gauche  → ajouter '0' tjrs de la racine
        - Aller à droite → ajouter '1'
        - À chaque feuille, enregistrer le code obtenu

    Returns:
        Dict[str, str]: table {caractère : code binaire}
        Dict[str, str]: c un  Dictionnaire mappant chaque caractère à son code binaire
        str 1: c de char
        str 2: code binaire 
    """
    if( verifier_arbre_huffman(racine) == False):
        raise ValueError("L'arbre de Huffman fourni est incorrect.")
    
    # Créer un dictionnaire pour stocker les codes de Huffman (tables de codage )
    # Table des codes de Huffman 
    table_codage: Dict[str, str] = {}
    
    #  créer fonction qui parcourt les noeuds
    def parcourir_noeud(noeud: Optional[Noeud], code_courant: str) -> None:
        """
        Parcours récursif de l'arbre pour construire les codes binaires.
        """
        if noeud is None:
            return
 
        # Si le nœud est une feuille,enregistrer le code cad  ajouter le {caractere: code} à la table.
        if noeud.est_feuille() and noeud.caractere is not None:
            table_codage[noeud.caractere] = code_courant
            return
        #   Sinon :
        # Appelle récursivement gauche avec code + "0"
        # Appelle récursivement droite avec code + "1"
        # Parcourir les enfants gauche et droit
        parcourir_noeud(noeud.gauche, code_courant + "0")
        parcourir_noeud(noeud.droit, code_courant + "1")

    parcourir_noeud(racine, "")
    # Résultat : dictionnaire table_codage = {'e':'10', ' ':'0', 'o':'111', ...} par exple
    return table_codage



# -------------------------------
# Étape 2 : Encoder le texte
# -------------------------------

def encoder_texte():
    """
    Encode le texte original en utilisant la table de codage Huffman.
    Étapes :
    1. Lire le texte original     2. Générer la table de codage  3. Remplacer chaque caractère par son code binaire
    """
    # Lire le texte original
    texte_original = lire_fichier("test.txt")
    # Récupérer l'arbre de Huffman
    racine = recuperer_arbre_huffman()
    # Parcourir chaque caractère : code_bin = table_codage[caractere]
    table_codage = generer_codes_huffman(racine)
    # Concaténer tous les codes binaires dans une chaîne unique
    texte_encode = ''.join(table_codage[char] for char in texte_original)
    # Résultat : texte_encode = "010011101..."
    return texte_encode

# -------------------------------
# Étape 3 : Sauvegarder le texte encodé
# -------------------------------

def sauvegarder_texte_encode(texte_encode: str, nom_fichier: str) -> None:
    """
    Sauvegarde le texte encodé .

    Args:
        texte_encode (str): Texte encodé en binaire
        nom_fichier (str): Nom du fichier de sortie
    #     """
    # Ouvrir un fichier en mode écriture binaire ('w')
    # ajouter "compressé" à la fin du nom de fichier avant l'extension .txt
    with open(nom_fichier[:nom_fichier.rfind('.')]+"_compressé."+nom_fichier[nom_fichier.rfind('.')+1:], 'w') as fichier:
    # Écrire la chaîne binaire dans le fichier
        fichier.write(texte_encode)
    # Vérifie que taille_fichier_encodé < taille_fichier_original (gain de compression attendu)
    taille_original = len(lire_fichier("test.txt")) * 8  # en bits (1 caractère = 8 bits)
    taille_encode = len(texte_encode)  # en bits
    print(f"Taille fichier original : {taille_original} bits")
    print(f"Taille fichier encodé : {taille_encode} bits")
    if taille_encode < taille_original:
        print("Compression réussie !")
    else:
        print("Aucune compression obtenue.")

# -------------------------------
# Étape 4 : Test de la partie encodage
# -------------------------------

# Vérifier que chaque caractère du texte a un code
def verifier_codes_caracteres(table_codage: Dict[str, str], texte: str) -> bool:
    for char in texte:
        if char not in table_codage:
            return False
    return True
# Vérifier que aucun code n’est préfixe d’un autre (propriété Huffman)
def verifier_propriete_prefixe(table_codage: Dict[str, str]) -> bool:
    codes = list(table_codage.values())
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j and codes[j].startswith(codes[i]):
                return False
    return True
# Vérifier que le texte encodé n’est pas vide
def verifier_texte_encode_non_vide(texte_encode: str) -> bool:
    return len(texte_encode) > 0



if __name__ == '__main__':
    # Générer l'arbre de Huffman
    racine = recuperer_arbre_huffman()
    # Générer les codes de Huffman
    table_codage = generer_codes_huffman(racine)
    # Encoder le texte
    texte_encode = encoder_texte()
    # Sauvegarder le texte encodé
    sauvegarder_texte_encode(texte_encode, "texte_encode.txt")
    # Vérifications
    texte_original = lire_fichier("test.txt")
    assert verifier_codes_caracteres(table_codage, texte_original), "Erreur : Un caractère n'a pas de code."
    assert verifier_propriete_prefixe(table_codage), "Erreur : La propriété de préfixe est violée."
    assert verifier_texte_encode_non_vide(texte_encode), "Erreur : Le texte encodé est vide."
    print("Tous les tests d'encodage sont passés avec succès.")
   