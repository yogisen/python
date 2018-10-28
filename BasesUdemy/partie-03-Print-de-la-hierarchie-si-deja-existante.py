import os
import json

# Fonction qui print la hiérarchie de dossiers à partir d'un fichier JSON
def print_hierarchie(fichier_json):
	with open(fichier_json, 'r') as f:
		structure = json.load(f)
	print('Les dossiers existent deja.')
	print('Voici la hierarchie de dossier:')
	for key, values in structure.items():
		print('. {0}'.format(key))
		for value in values:
			print('--- {0}'.format(value))

		print('='*25)

# Fonction qui passe à travers le dictionnaire et créé les dossiers / sous-dossiers
def creer_dossiers(dossiers):
	for key, values in dossiers.items():
		for value in values:
			dossier = '{0}/{1}/{2}'.format(base, key, value)
			os.makedirs(dossier)
			print('Creation du dossier {0}'.format(dossier))

# Fonction qui écrit le dictionnaire dans le fichier JSON
def ecrire_json(fichier_json, dictionnaire):
	with open(fichier_json, 'w') as f:
		json.dump(dictionnaire, f, indent=4)

# Chemin dans lequel on créé la structure de dossiers
base = r'C:\Users\Thibh\Desktop\Structure'
base = base.replace('\\', '/')

# Chemin vers le fichier JSON
fichier_json = r'C:\Users\Thibh\Desktop\Structure\structure.json'
fichier_json = fichier_json.replace('\\', '/')

# Création du dictionnaire de dossiers / sous-dossiers
structure = {
			 'Musique': ['Rock', 'Jazz', 'Pop'],
			 'Documents': ['Factures', 'Travail', 'Maison'],
			 'Images': ['Vacances', 'Famille'],
			 'Videos': ['Chat', 'Facebook']
			}

# On vérifie si le fichier existe déjà
if os.path.isfile(fichier_json):
	# Si le fichier existe déjà, on print la hiérarchie à partir du fichier JSON
	print_hierarchie(fichier_json)
else:
	# Si le fichier JSON n'existe pas, on créé la hiérarchie et on écrit
	# le fichier JSON
	creer_dossiers(structure)
	ecrire_json(fichier_json, structure)