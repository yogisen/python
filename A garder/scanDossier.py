import os
import json

# On défini un dossier de départ
dossier_de_depart = "/home/yogi/Documents"

# On créé une liste vide qui va contenir les fichiers
liste_de_fichiers = []
# On boucle à travers tous les dossiers, sous-dossiers et fichiers
for root, dirs, files in os.walk(dossier_de_depart):
    # On boucle à travers les fichiers
    for fichier in files:
        liste_de_fichiers.append(os.path.join(root, fichier))

# On défini le chemin du fichier JSON
chemin_fichier = "/home/yogi/Bureau/documents_listes.json"
# On écrit la liste de fichiers dans le fichier JSON.
with open(chemin_fichier, 'w') as f:
	# On utilise l'argument 'indent=4' pour rendre le fichier JSON plus lisible.
	json.dump(liste_de_fichiers, f, indent=4)


