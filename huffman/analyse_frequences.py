from collections import Counter


#compter la frequence de chaque caractere 
def analyser_frequences(texte):
    return dict(Counter(texte))


#afficher les frequence 
def afficher_frequences(frequences):
  
    print("Frequences des caracteres:")
    for char, freq in sorted(frequences.items(), key=lambda x: x[1], reverse=True):
        c = '␣' if char == ' ' else char
        print(f"  {c}: {freq}")



# la lecture d un fichier
def lire_fichier(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()