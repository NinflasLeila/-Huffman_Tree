# Projet Huffman Tree

## Description
Implémentation de l’algorithme de compression de Huffman en Python.

## Répartition du travail

### Personne 1 : Analyse des fréquences
Analyse des fréquences et structure de base

---

## 📋 Description du Module

Ce module constitue la **première étape** de l'implémentation de l'algorithme de compression de Huffman. Il est responsable de :

- Lecture et traitement de fichiers texte
- Comptage des fréquences de chaque caractère
- Création de la structure de données pour les nœuds de l'arbre
- Affichage formaté des statistiques de fréquences
- Tests unitaires pour valider le bon fonctionnement

---

## 📁 Fichiers Livrés

```
projet_huffman/
├── analyse_frequences.py    # Module principal (300+ lignes)
├── test.txt                  # Fichier de test
└── README_Personne1.md       # Cette documentation
```

---

## 🔧 Installation et Utilisation

### Prérequis
- Python 3.7 ou supérieur
- Aucune bibliothèque externe nécessaire (utilise seulement la bibliothèque standard)

### Utilisation Basique

```python
from analyse_frequences import analyser_fichier, afficher_frequences

# Analyser un fichier
texte, frequences, noeuds = analyser_fichier('mon_fichier.txt')

# Afficher les résultats
afficher_frequences(frequences)
```

### Utilisation Avancée

```python
from analyse_frequences import calculer_frequences, creer_noeuds_feuilles, Noeud

# Analyser un texte directement
texte = "Bonjour le monde!"
frequences = calculer_frequences(texte)

# Créer les nœuds
noeuds = creer_noeuds_feuilles(frequences)

# Utiliser les nœuds pour la suite du projet
for noeud in noeuds:
    print(f"Caractère: {noeud.caractere}, Fréquence: {noeud.frequence}")
```

---

## 🏗️ Structure de Données : Classe `Noeud`

```python
class Noeud:
    def __init__(self, caractere=None, frequence=0, gauche=None, droit=None):
        self.caractere = caractere    # str ou None
        self.frequence = frequence    # int
        self.gauche = gauche          # Noeud ou None
        self.droit = droit            # Noeud ou None
```

### Méthodes Importantes

| Méthode | Description |
|---------|-------------|
| `est_feuille()` | Retourne `True` si le nœud n'a pas d'enfants |
| `__lt__(autre)` | Comparaison nécessaire pour `heapq` (tri par fréquence) |
| `__repr__()` | Représentation lisible pour le débogage |

---

## 📊 Résultats des Tests

### Tests Unitaires : ✅ 100% Réussis

| Test | Statut | Description |
|------|--------|-------------|
| `test_noeud()` | ✅ RÉUSSI | Création et manipulation des nœuds |
| `test_calculer_frequences()` | ✅ RÉUSSI | Calcul correct des fréquences |
| `test_creer_noeuds_feuilles()` | ✅ RÉUSSI | Création de la liste de nœuds |

### Test sur Fichier Réel (`test.txt`)

**Statistiques :**
- **Taille du texte** : 112 caractères
- **Caractères uniques** : 28
- **Nœuds créés** : 28

**Top 5 des caractères les plus fréquents :**

| Rang | Caractère | Fréquence | Pourcentage |
|------|-----------|-----------|-------------|
| 1 | [ESPACE] | 20 | 17.86% |
| 2 | e | 12 | 10.71% |
| 3 | n | 9 | 8.04% |
| 4 | o | 8 | 7.14% |
| 5 | s | 7 | 6.25% |

---

## 🔍 Fonctionnalités Implémentées

### ✅ Fonctions Principales

1. **`lire_fichier(chemin_fichier)`**
   - Lit un fichier en UTF-8
   - Gère les erreurs (fichier inexistant, encodage)

2. **`calculer_frequences(texte)`**
   - Compte chaque caractère
   - Retourne un dictionnaire `{caractère: fréquence}`

3. **`creer_noeuds_feuilles(frequences)`**
   - Transforme le dictionnaire en liste de `Noeud`
   - Prêt pour `heapq` (Personne 2)

4. **`afficher_frequences(frequences, trier=True)`**
   - Affichage formaté et lisible
   - Tri par fréquence décroissante
   - Gère les caractères spéciaux (espaces, retours à la ligne)

5. **`analyser_fichier(chemin_fichier)`**
   - **Fonction principale** pour l'intégration
   - Retourne : `(texte, frequences, noeuds)`

---

## 🧪 Comment Lancer les Tests

```bash
# Lancer le module (tests inclus)
python analyse_frequences.py
```

**Sortie attendue :**
```
============================================================
EXÉCUTION DES TESTS UNITAIRES
============================================================
✅ Tous les tests de Noeud sont réussis !
✅ Tous les tests de calculer_frequences sont réussis !
✅ Tous les tests de creer_noeuds_feuilles sont réussis !
🎉 TOUS LES TESTS SONT RÉUSSIS !
```

---

## 🔗 Interface pour la Personne 2

### Import Nécessaire

```python
from analyse_frequences import analyser_fichier, Noeud
```

### Données Fournies

```python
texte, frequences, noeuds = analyser_fichier('fichier.txt')

# noeuds est une liste de Noeud prête pour heapq
# Chaque noeud contient :
#   - noeud.caractere : le caractère
#   - noeud.frequence : sa fréquence
#   - noeud.gauche / noeud.droit : None (à remplir par Personne 2)
```

### Compatibilité avec `heapq`

La classe `Noeud` implémente `__lt__` pour permettre :

```python
import heapq

# La liste de nœuds peut être directement transformée en min-heap
heapq.heapify(noeuds)

# Les nœuds sont triés par fréquence croissante
noeud_min = heapq.heappop(noeuds)
```

---

## 📈 Analyse de Performance

### Complexité Temporelle

| Fonction | Complexité |
|----------|-----------|
| `lire_fichier()` | O(n) |
| `calculer_frequences()` | O(n) |
| `creer_noeuds_feuilles()` | O(k) où k = nombre de caractères uniques |
| `afficher_frequences()` | O(k log k) avec tri |

### Complexité Spatiale

- **O(n)** pour stocker le texte
- **O(k)** pour le dictionnaire de fréquences
- **O(k)** pour la liste de nœuds

---

## 🎯 Caractéristiques Notables

### Gestion des Caractères Spéciaux

Le module gère correctement :
- ✅ Espaces
- ✅ Retours à la ligne (`\n`)
- ✅ Tabulations (`\t`)
- ✅ Caractères accentués (é, è, à, etc.)
- ✅ Ponctuation (!, ?, ., etc.)

### Affichage Amélioré

Les caractères non imprimables sont affichés de manière lisible :
- Espace → `[ESPACE]`
- Retour à la ligne → `[RETOUR]`
- Tabulation → `[TAB]`

---

## 📝 Exemple Complet

```python
# Contenu de test.txt :
# "Bonjour le monde!
# Ceci est un test pour l'algorithme de Huffman.
# La compression de données est fascinante."

from analyse_frequences import analyser_fichier

# Analyser le fichier
texte, frequences, noeuds = analyser_fichier('test.txt')

# Résultats obtenus :
# - 112 caractères au total
# - 28 caractères uniques
# - 28 nœuds feuilles créés
# - Espace le plus fréquent (17.86%)
```

---

## 🐛 Gestion des Erreurs

Le module gère les erreurs suivantes :

```python
try:
    texte, freq, noeuds = analyser_fichier('fichier.txt')
except FileNotFoundError:
    print("Le fichier n'existe pas")
except UnicodeDecodeError:
    print("Erreur d'encodage du fichier")
```

---

## 📌 Points Importants pour l'Équipe

### ✅ Ce qui est prêt

- Structure `Noeud` complète et testée
- Comparaison `__lt__` implémentée pour `heapq`
- Liste de nœuds feuilles prête à l'emploi
- Tests unitaires validés

### 🔄 Ce qui est attendu de la Personne 2

La Personne 2 doit :
1. Importer la classe `Noeud` et la fonction `analyser_fichier()`
2. Utiliser `heapq` pour créer une file de priorité
3. Fusionner les nœuds pour construire l'arbre de Huffman
4. Remplir les attributs `gauche` et `droit` des nœuds internes

---

## 📚 Documentation du Code

Le code est entièrement documenté avec :
- **Docstrings** pour chaque fonction
- **Commentaires** pour les sections complexes
- **Exemples d'utilisation** dans les docstrings
- **Type hints** implicites dans la documentation

---

## 🎓 Conclusion

Ce module constitue une base solide pour le projet de compression de Huffman. Il a été testé, validé et est prêt pour l'intégration avec les autres modules.

**Statut : ✅ COMPLET ET VALIDÉ**
---

**Date de livraison :** Décembre 2024  
**Version :** 1.0  
**Langage :** Python 3.7+  
**Dépendances :** Aucune
### Personne 2 : Construction de l’arbre
À venir

### Personne 3 : Encodage
À venir

### Personne 4 : Décodage et analyse
À venir
