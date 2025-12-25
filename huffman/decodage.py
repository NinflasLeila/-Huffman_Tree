def decoder(texte_encode, racine):
    resultat = []
    noeud = racine

    for bit in texte_encode:
        noeud = noeud.gauche if bit == '0' else noeud.droite
        if noeud.char is not None:
            resultat.append(noeud.char)
            noeud = racine

    return "".join(resultat)

def calculer_stats(texte_original, texte_encode):
    original = len(texte_original) * 8
    compresse = len(texte_encode)
    taux = compresse / original
    gain = 1 - taux

    print("\nSTATISTIQUES")
    print(f"Taille originale  : {original} bits")
    print(f"Taille compressée : {compresse} bits")
    print(f"Taux compression  : {taux:.2%}")
    print(f"Gain              : {gain:.2%}")

def sauvegarder(texteencode,chemin):
    with open(chemin,"w") as f:
        f.write(texteencode)
        