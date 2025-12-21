## **🎯 Objectif général de ta partie**
## Objectif Général
<strong>
<span style="color:Blue;">  Tâche à Faire:  Encodage et génération des codes  </span>  Par:
<span style="color:red;">  Personne 3: SIHAM TAYEBI </span>
</strong>


##### Ce module a pour but de transformer un arbre de Huffman en codes binaires, puis d’encoder un texte caractère par caractère pour produire un fichier compressé.

Il s’appuie sur :

 - l’analyse des fréquences (Personne 1: Noha sabih)

 - la construction de l’arbre de Huffman (Personne 2 : ELBATOUL HNAGANAG)

## **📊Objectifs Spécifiques** 
&nbsp;&nbsp;&nbsp;&nbsp;▼ 

- <span style="color:green;">**Génération des codes binaires pour chaque caractère (parcours de l'arbre)** :</span> 
- <span style="color:blue;">**Générer les codes binaires pour chaque caractère à partir de l’arbre de Huffman.** :</span> 
- <span style="color:orange;">**Créer une table de codage optimisée (dictionnaire {caractère: code binaire}).** :</span> 
- <span style="color:red;">**Encoder le texte original en binaire.** :</span>   
- <span style="color:purple;">**Sauvegarder le texte encodé dans un fichier.** :</span> 
- <span style="color:brown;">**Vérifier la validité de l’encodage avec des tests (caractères codés, propriété de préfixe, texte non vide).** :</span> 
*Transformer l’arbre de Huffman en codes binaires et encoder le texte*
#### ⚠️TAF: Arbre(Faite par Personne2: ELBATOUL HNAGNAG) → codes → texte binaire

---

## ✅ ÉTAPE 1 : Comprendre l’arbre & Génération de l’arbre de Huffman
- Fonction : recuperer_arbre_huffman()

- Principe :

 * Récupérer les fréquences depuis le fichier texte.

 * Créer les nœuds feuilles pour chaque caractère.

 * Construire l’arbre de Huffman final.

 + frequences = analyser_fichier("test.txt")[1]
 + racine = construire_arbre_huffman(creer_noeuds_feuilles(frequences))


- Remarque :
Seules les fréquences sont utilisées pour reconstruire l’arbre, ce qui garantit l’indépendance du module et la cohérence avec l’analyse des fréquences.

==========================================================================================================

- Et chaque :
 - **feuille = caractère**
 - **gauche = 0**
 - **droite = 1**
- Un chemin :
 - **Racine → gauche → droite → feuille**
- donne :
 - **0 1**

---

## ✅ ÉTAPE 2 : Parcourir l’arbre (idée clé) & Vérification de l’arbre
- Fonction : verifier_arbre_huffman(racine)
- Objectif : Vérifier que l’arbre est valide selon la structure Huffman :
- Feuille : contient un caractère et une fréquence > 0
- Nœud interne : ne contient pas de caractère, possède deux enfants
- Vérification récursive de tous les sous-arbres
```
if racine.est_feuille():
    return racine.caractere is not None and racine.frequence > 0
```

============================================================================================

+ **parcourir l’arbre récursivement**
+ **accumuler un chemin binaire**
+ **dès qu'on  arrive à une feuille on doit:**
  - stocker le code
+ 👉 Résultat :
  - **{'e': '10', ' ': '0', 'o': '111'}**
⚠️ NB :
+ **Cette étape est faite UNE SEULE FOIS pour ne pas refaire la même chose à chaque fois rechercher le même noeud déjà recherché pour optimiser de la recherche**
+ **Prof SARA RETAL appelle ça encodage amélioré dans le doc "PROJET DE FIN DE MODULE - Structure de donnees"**

---

## ✅ ÉTAPE 3 : Créer la table de codage
- Fonction : generer_codes_huffman(racine)
- Principe :
 * Parcours récursif de l’arbre.
 * Aller à gauche → ajouter '0', aller à droite → ajouter '1'.
 * À chaque feuille, le code est stocké dans le dictionnaire table_codage.
 * table_codage[noeud.caractere] = code_courant

Exemple de résultat :
``` 
{'e': '10', ' ': '0', 'o': '111'}
```

**Remarque :**
Le parcours se fait une seule fois, ce qui permet un encodage rapide et évite de recalculer les codes pour chaque caractère.

============================================================================================


- Pourquoi créer la ?
 * **Pour éviter de parcourir l’arbre pour  chaque caractère**
 * **Pour être rapide et propre**
⚠️ NB : **« On pré-calcule les codes pour optimiser l’algorithme »**

---

## ✅ ÉTAPE 4 : Encodage du texte
Méthode suivie :
  * **Lire le texte original**
  * **Pour chaque caractère :**
    + prendre son code dans la table
    + concaténer les bits
  
**Principe :**
 * Lire le texte original (lire_fichier).
 * Générer la table de codage (generer_codes_huffman).
 * Remplacer chaque caractère par son code binaire.
 * Concaténer les codes pour obtenir une chaîne binaire unique.
 * texte_encode = ''.join(table_codage[char] for char in texte_original)
**Résultat attendu :**
 * 010011101...

---

## ✅ ÉTAPE 5 : Sauvegarde du texte encodé

On doit:
 - **écrire la chaîne binaire dans un fichier par exple test_compresse.txt**
 - **prouver que ça fonctionne sur test.txt**

Fonction : sauvegarder_texte_encode(texte_encode, nom_fichier)
Principe :
 - Ajouter _compressé au nom de fichier original.
 - Écrire le texte encodé dans un fichier.
 - Vérifier que le texte compressé est plus petit que le texte original (gain de compression).
 - taille_original = len(lire_fichier("test.txt")) * 8
 - taille_encode = len(texte_encode)

Affichage :
 - Taille fichier original : 3200 bits
 - Taille fichier encodé : 2100 bits
Compression réussie !

---

## ✅ Étape 6 — Vérifications et tests

Objectif : S’assurer de la validité de l’encodage :

 - Chaque caractère du texte a un code.

 - verifier_codes_caracteres(table_codage, texte_original)
 - Propriété de Huffman : aucun code n’est préfixe d’un autre.

 - verifier_propriete_prefixe(table_codage)
 - Texte encodé non vide.
 - verifier_texte_encode_non_vide(texte_encode)

Tous les tests sont exécutés à la fin du script principal (if __name__ == '__main__':).

## ✅ Conclusion

Cette partie du projet permet de :

 + Générer automatiquement les codes Huffman pour chaque caractère.

 + Encoder un texte en binaire de manière efficace.

 + Sauvegarder le résultat compressé.

 + Vérifier la validité et la fiabilité du processus.

 + Elle complète le flux global de compression :

 + Arbre Huffman (Personne 2) → Codes binaires → Texte compressé

 🏁 **Cette partie permet de finaliser le processus de compression Huffman en transformant une structure arborescente en une représentation binaire compacte, optimisée et exploitable.
L’implémentation respecte les principes fondamentaux de l’algorithme de Huffman et garantit des performances optimales.**
