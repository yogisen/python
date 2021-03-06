import os
import json


def print_hierarchie(fichier_json):
    with open(fichier_json, 'r') as f:
        structure = json.load(f)
    print('les dossier existent deja. ')
    print('Voici la hierarchie de dossier')
    for key, values in structure.items():
        print('. {0}'.format(key))
        for value in values:
            print ('----{0}'.format(value))

        print('='*25)

def creer_dossier(dossiers):
    for key, values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key, value)
            print('creation du dossier{0}'.format(dossier))
            os.makedirs(dossier)

def ecrire_json(fichier_json, dictionnaire):
    with open(fichier_json, 'w') as  f:
        json.dump(dictionnaire, f, indent=4)

base = r'C:\Users\Selim.NASRI\Desktop\Repertoires'
base = base.replace('\\', '/')

fichier_json = r'C:\Users\Selim.NASRI\Desktop\Repertoires\structures.json'
fichier_json = fichier_json.replace('\\', '/')

Structure = {
            'Musique': ['Rock', 'Jazz', 'Pop'],
            'Documents': ['Mes document', 'Maison', ],
            'Images': ['Vacances'],
            'Cours': ['Python', 'django']
            }

if os.path.isfile(fichier_json):
    print_hierarchie(fichier_json)
else:
    creer_dossier(Structure)
    ecrire_json(fichier_json, Structure)