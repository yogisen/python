liste = ['U', 'd', 'e', 'm', 'y']

# Tableau qui représente les indices (en haut) et les slices (en bas)

  -5  -4  -3  -2  -1
  0   1   2   3   4
+---+---+---+---+---+
| U | d | e | m | y |
+---+---+---+---+---+
0   1   2   3   4   5

# Pour récupérer une lettre en particulier:
liste[2]
>>> 'e'

liste[-3]
>>> 'e'

# Pour récupérer un ou plusieurs éléments avec les slices:
liste[0:2]
>>> ['U', 'd']

liste[:2]
>>> ['U', 'd']

liste[3:]
>>> ['m', 'y']