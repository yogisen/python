import os
from random import randint

directory = 'home/yogi/Documents/test/'

def checkDirectory(path, lookFor):
    content = os.listdir(path)
    # On regarde tout le contenu du repertoire indique
    for file in content:
        # on ne retient que les fichiers .txt
        if file.endswith('.txt'):
            with open(path + '/' + file, 'r') as f:
                # on check les lignes une par une pour voir si elles correspondent a notre recherche.
                # grace a enumerate on a aussi les numeros de ligne
                for idx, line in enumerate(f.readlines()):
                    # ici, line.rstrip() sert simplement a degager le retour a la ligne a la fin de chaque ligne
                    line = line.rstrip()
                    if line == lookFor:
                        # si la ligne correspond, on la renvoie dans le generateur
                        yield idx, file
                        # sans le break, tu auras un retour pour chaque fois qu'une ligne correspond a ta recherche dans un meme fichier.
                        # avec le break, la recherche s'arretera au premier resultat
                        break


for idx, file in checkDirectory(directory, 'dns = 6.6.6.6'):
    print (idx, file)