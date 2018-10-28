import os

def creer_dossier(dossiers):
    for key, values in dossiers.items():
        for value in values:
            dossier = '{0}/{1}/{2}'.format(base, key, value)
            print('creation du dossier{0}'.format(dossier))
            os.makedirs(dossier)

base = r'C:\Users\Selim.NASRI\Desktop\Repertoires'
# pour eviter les erreur je vais remplacer les \ windows < Linux
base = base.replace('\\', '/')

Structure = {
            'Musique': ['Rock', 'Jazz', 'Pop'],
            'Documents': ['Mes document', 'Maison', ],
            'Images': ['Vacances'],
            'Cours': ['Python', 'django']
            }

creer_dossier(Structure)