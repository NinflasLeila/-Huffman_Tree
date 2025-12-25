from analyse_frequences import lire_fichier, analyser_frequences, afficher_frequences
from construction_arbre import construire_arbre
from encodage import generer_codes, encoder, afficher_codes
from decodage import decoder, calculer_stats , sauvegarder


def main():
    print("=== CODAGE DE HUFFMAN (FICHIER) ===")

    # read file 
    texte = lire_fichier("test.txt")

    print(f"\nTexte original ({len(texte)} caractères)\n")

    frequences = analyser_frequences(texte)
    afficher_frequences(frequences)

    arbre = construire_arbre(frequences)

    codes = generer_codes(arbre)
    afficher_codes(codes)

    texte_encode = encoder(texte, codes)
    texte_decode = decoder(texte_encode, arbre)

    print("\n✓ Décodage correct" if texte == texte_decode else "✗ Erreur de décodage")

    calculer_stats(texte, texte_encode)

    sauvegarder(texte_encode, "texte_encode.txt")


if __name__ == "__main__":
    main()
