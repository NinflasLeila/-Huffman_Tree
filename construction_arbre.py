"""
Module de construction de l'arbre de Huffman
Auteur: Personne 2
Description: Construction de l'arbre de Huffman à partir des nœuds feuilles
"""

import heapq # Importation du module heapq pour la gestion du tas min (priority queue 
# une min-heap)
from typing import List, Optional # Importation des types List et Optional pour les annotations de type
from analyse_frequences import Noeud, creer_noeuds_feuilles  # Importation de la classe Noeud et de la fonction creer_noeuds_feuilles


def construire_arbre_huffman(noeuds_feuilles: List[Noeud]) -> Optional[Noeud]:
    """
    Construit l'arbre de Huffman à partir d'une liste de nœuds feuilles.

    Algorithme :
        - On place tous les nœuds feuilles dans un tas min (heap)
        - Tant qu'il y a plus d'un nœud dans le tas :
            * on extrait les deux nœuds de plus petite fréquence
            * on crée un nœud parent dont la fréquence est la somme
            * on insère ce nœud parent dans le tas
        - Le dernier nœud restant est la racine de l'arbre de Huffman

    Args:
        noeuds_feuilles (list[Noeud]): Liste de nœuds feuilles (un par caractère)

    Returns:
        Noeud | None: Racine de l'arbre de Huffman, ou None si la liste est vide
    """
    if not noeuds_feuilles:
        return None

    heap = noeuds_feuilles[:]      # copie pour ne pas modifier l'original
    heapq.heapify(heap)            # tas min basé sur Noeud.frequence

    while len(heap) > 1:
        gauche = heapq.heappop(heap)#Supprime et retourne le plus petit élément du tas (heap)
        # Taille du heap diminue de 1 à chaque heappop
        droit = heapq.heappop(heap)

        frequence_totale = gauche.frequence + droit.frequence
        parent = Noeud(
            caractere=None,        # nœud interne
            frequence=frequence_totale,
            gauche=gauche,
            droit=droit
        )

        heapq.heappush(heap, parent)
        """Ajoute un nouvel élément dans le tas
        Taille du heap augmente de 1
        L’ordre du tas est automatiquement conservé (min-heap : plus petit en haut)"""
    """On retire 2 nœuds → len(heap) diminue de 2
    On ajoute 1 nœud → len(heap) augmente de 1
    heap = [c(1), a(2), b(3)]
    Nouveau heap :

    heap = [b(3), *(3)]
    len(heap) = 2"""
    return heap[0]

# Optional[Noeud] signifie :
# soit c’est un Noeud
# soit c’est None (arbre vide)

# indent → chaîne de caractères utilisée pour l’indentation
# Défaut = "" → pas d’espace au départ

# branche → indique la position du nœud :

# "R" → racine (root)
# "G" → nœud gauche
# "D" → nœud droit

# 3️⃣ -> None
# Signifie que la fonction ne renvoie rien
# Elle sert uniquement à afficher l’arbre dans la console
def afficher_arbre(racine: Optional[Noeud], indent: str = "", branche: str = "R") -> None:
    """
    Affiche l'arbre de Huffman de manière lisible (texte).

    Args:
        racine (Noeud | None): Racine de l'arbre
        indent (str): Indentation (utilisée en interne pour la récursion)
        branche (str): Indique si le nœud est R(acine), G(auche) ou D(roite)
    """
    if racine is None:
        print("(arbre vide)")
        return

    # Affiche le nœud courant
    if racine.caractere is None:
        etiquette = f"* (freq={racine.frequence})"   # nœud interne
    else:
        etiquette = f"'{racine.caractere}' (freq={racine.frequence})"

    print(f"{indent}[{branche}] {etiquette}")

    # Appel récursif sur les enfants
    if racine.gauche is not None:
        afficher_arbre(racine.gauche, indent + "   ", "G")
    if racine.droit is not None:
        afficher_arbre(racine.droit, indent + "   ", "D")


# ==================== TESTS UNITAIRES ====================

def test_construction_arbre_simple():
    """Test simple de la construction de l'arbre de Huffman."""
    print("\n🧪 Test : construire_arbre_huffman (cas simple)")

    frequences = {'a': 5, 'b': 1, 'c': 1}
    feuilles = creer_noeuds_feuilles(frequences)
    racine = construire_arbre_huffman(feuilles) # Construire l'arbre de Huffman , insérer les feuilles et obtenir la racine
    

    assert racine is not None, "Échec : la racine ne doit pas être None"
    frequence_totale = sum(frequences.values())
    assert racine.frequence == frequence_totale, (
        f"Échec : fréquence totale incorrecte (attendu {frequence_totale}, "
        f"obtenu {racine.frequence})"
    )

    print("✅ Test construction de l'arbre réussi")


def test_cas_un_seul_caractere():
    """Test du cas particulier où il n'y a qu'un seul caractère."""
    print("\n🧪 Test : cas un seul caractère")

    frequences = {'x': 10}
    feuilles = creer_noeuds_feuilles(frequences)
    racine = construire_arbre_huffman(feuilles)

    assert racine is not None, "Échec : racine None pour un seul caractère"
    assert racine.frequence == 10, "Échec : fréquence incorrecte pour la racine"
    assert racine.est_feuille(), "Échec : pour un seul caractère, la racine doit être une feuille"

    print("✅ Test cas un seul caractère réussi")


def executer_tous_les_tests():
    """Exécute tous les tests unitaires du module."""
    print("\n" + "="*60)
    print("EXÉCUTION DES TESTS UNITAIRES - CONSTRUCTION_ARBRE")
    print("="*60)

    test_construction_arbre_simple()
    test_cas_un_seul_caractere()

    print("="*60)
    print("🎉 TOUS LES TESTS DE CONSTRUCTION_ARBRE SONT RÉUSSIS !")
    print("="*60 + "\n")


# ==================== EXEMPLE D'UTILISATION ====================

if __name__ == "__main__":
    executer_tous_les_tests()

    print("\n" + "="*60)
    print("EXEMPLE D'UTILISATION DE L'ARBRE DE HUFFMAN (AFFICHAGE)")
    print("="*60 + "\n")

    texte = "Bonjour le monde"
    frequences = {}
    for c in texte:
        frequences[c] = frequences.get(c, 0) + 1

    feuilles = creer_noeuds_feuilles(frequences)
    racine = construire_arbre_huffman(feuilles)

    print("Texte :", texte)
    print("Fréquences :", frequences)
    print("\nArbre de Huffman construit :\n")
    afficher_arbre(racine)
