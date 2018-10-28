import os
import json

def creer_dossiers(dossiers):
    for key, values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key, value)
            print('Creation du dossier {0}'.format(dossier))
            os.makedirs(dossier)

def ecrire_json(fichier_json, dictionnaire):
    with open(fichier_json, 'w') as f:
        json.dump(dictionnaire, f, indent=4)
    print('Ecriture du fichier json.')

base = r'C:\Users\Thibh\Desktop\Structure'
base = base.replace('\\', '/')

fichier_json = r'C:\Users\Thibh\Desktop\Structure\structure.json'
fichier_json = fichier_json.replace('\\', '/')

structure = {
             'Musique': ['Rock', 'Jazz', 'Pop'],
             'Documents': ['Factures', 'Travail', 'Maison'],
             'Images': ['Vacances', 'Famille'],
             'Videos': ['Concert', 'Chat', 'Facebook']
            }


creer_dossiers(structure)
ecrire_json(fichier_json)






