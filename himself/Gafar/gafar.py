import os
import json

dossier_de_depart = "/home/yogi/Documents/test"
liste_de_fichiers = []

for root, dirs, files in os.walk(dossier_de_depart):
    for fichier in files:
        liste_de_fichiers.append(os.path.join(root, fichier))

chemin_fichier = "/home/yogi/Bureau/liste_fichiers_dns.json"
with open(chemin_fichier, 'w') as f:
    json.dump(liste_de_fichiers, f, indent=4)

print(liste_de_fichiers)
#['/home/yogi/Documents/test/Document 1 sans titre', '/home/yogi/Documents/test/Document 1 sans titre (3e copie)',