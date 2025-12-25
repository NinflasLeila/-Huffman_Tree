def generer_codes(racine):
    codes = {}

    def parcourir(noeud, code):
        if noeud.char is not None:
            codes[noeud.char] = code or "0"
        else:
            parcourir(noeud.gauche, code + "0")
            parcourir(noeud.droite, code + "1")

    parcourir(racine, "")
    return codes

def encoder(texte, codes):
    return "".join(codes[char] for char in texte)

def afficher_codes(codes):
    print("\nTable des codes:")
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        c = '␣' if char == ' ' else char
        print(f"  {c}: {code}")
