import glob
import os
from random import randint

directory = 'home/yogi/Documents/test'

def checkDirectory(path, lookFor):
    content = os.listdir(path)
    # On regarde tout le contenu du repertoire indique
    for file in content:
        # on ne retient que les fichiers .txt
        if file.endswith('.txt'):
            with open(path + '/' + file, 'r') as f:
                # ici, line.rstrip() sert simplement a degager le retour a la ligne a la fin de chaque ligne
                if lookFor in [line.rstrip() for line in f.readlines()]:
                    # Si une des lignes du fichier correspond au texte qu'on cherche, on renvoie le fichier dans le generateur
                    yield file


for file in checkDirectory(directory, 'dns 1 = 6.6.6.6'):
    print(file)



'''
for file in os.listdir("/home/yogi/Documents/test"):
    if file.endswith('.txt'):
        print(file)
Document 1 sans titre (13e copie).txt
Document 1 sans titre (8e copie).txt
Document 1 sans titre (10e copie).txt
Document 1 sans titre (7e copie).txt
Document 1 sans titre (11e copie).txt
Document 1 sans titre (15e copie).txt
Document 1 sans titre (9e copie).txt
'''
#list_files = glob.glob('*.txt')
# print(list_files) # []
# marche pas !!!!
'''
with open("/home/yogi/Documents/test/*.txt", 'r') as f:
    if "DNS 1 = 4.4.4.4" in f.readlines():
        print("bravo")
    else:
        print("tantpis")
'''