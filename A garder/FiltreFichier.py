import os
import json

# On lit la liste des fichiers récupérés précédemment dans le fichier JSON

chemin_fichier = "/home/yogi/Bureau/documents_listes.json"
with open(chemin_fichier, 'r') as f:
    liste_fichiers = json.load(f)

# On créé une liste qui contient les extensions que l'on veut filtrer

fichiers_extensions = ['.jpg', '.pdf', '.all', '.rar']
liste_fichier_filtre = []

# On boucle à travers les fichiers

for fichier in liste_fichiers:
    # On récupère l'extension du fichier
    extension = os.path.splitext(fichier)[1]
    # Si l'extension est dans la liste images_extensions, on l'ajoute à la liste
    if extension in fichiers_extensions:
        liste_fichier_filtre.append(fichier)

        # export resultat
        document_filtre = "/home/yogi/Bureau/documents_filtre.json"
        # On écrit la liste de fichiers dans le fichier JSON.
        with open(document_filtre, 'w') as f:
            json.dump(liste_fichier_filtre , f, indent=4)

print(liste_fichier_filtre)



