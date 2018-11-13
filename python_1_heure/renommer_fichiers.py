# On importe les modules nécessaires à notre script
import os
import json
import time

# On lit la liste des fichiers récupérés précédemment dans le fichier JSON
chemin_fichier = r"C:\PythonEnUneHeure\liste_fichiers.json"
with open(chemin_fichier, 'r') as f:
	liste_fichiers = json.load(f)

# On créé une liste qui contient les extensions que l'on veut filtrer
images_extensions = ['.jpg', '.jpeg', '.tga', '.tif']
liste_fichier_filtre = []
# On boucle à travers les fichiers
for fichier in liste_fichiers:
	# On récupère l'extension du fichier
	extension = os.path.splitext(fichier)[1]
	# Si l'extension est dans la liste images_extensions, on l'ajoute à la liste
	if extension in images_extensions:
		liste_fichier_filtre.append(fichier)

# On boucle à travers les fichiers de type image
for fichier in liste_fichier_filtre:
	# On récupère la date de création du fichier
	t = os.path.getctime(fichier)
	# On la converti en date lisible
	t = time.ctime(t)
	# On remplace les espaces et les deux points par des tirets
	t = t.replace(' ', '_').replace(':', '-')
	# On récupère le nom du fichier et son extension
	nom, extension = os.path.splitext(fichier)
	# On remplace l'extension par la date de création du fichier + l'extension
	nouveau_nom_complet = fichier.replace(extension, '_' + t + extension)
	# On renomme le fichier
	os.rename(fichier, nouveau_nom_complet)


	