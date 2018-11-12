"""Les fichiers JSON nous permettent d'écrire et de lire des structures
de données complexes à l'intérieur de fichiers sur le disque. Pour
utiliser le module json il faut bien entendu commencer par l'importer"""
import json

# On défini ensuite un chemin vers un fichier json.
chemin_fichier = r"C:\PythonEnUneHeure\liste.json"

# On écrit à l'intérieur du fichier à l'aide de la méthode 'dump'
with open(chemin_fichier, 'w') as f:
	json.dump([1, 2, 3, 4, 5], f)

# Pour lire le fichier de nouveau, on utilise la méthode 'load'
with open(chemin_fichier, 'r') as f:
	ma_liste = json.load(f)