"""Quand vous déclarez un chemin vers un dossier sur Windows
vous allez vous heurter à un problème avec les slash.
En effet, le symbole \ en Python est utilisé pour 'échapper'
des symboles spéciaux, par exemple si vous voulez mettre une
apostrophe dans une chaîne de caractère"""
phrase = 'J\'adore programmer en Python'

"""Cela cause donc un problème avec les chemins sur Windows
si l'on ne met qu'un seul slash"""
chemin = 'C:\PythonEnUneHeure\fichier_a_lire.txt'
print(chemin)
# >>> C:\PythonEnUneHeureichier_a_lire.txt
"""Vous voyez avec l'exemple ci-dessus que le \f est transformé
en  et rend donc notre chemin incorrect. Pour remédier à
cela il existe trois solutions. La première est de doubler chaque slash"""
chemin = 'C:\\PythonEnUneHeure\\fichier_a_lire.txt'
"""Le premier slash va échapper le deuxième slash et donc éliminer le problème.
La deuxième méthode consiste à indiquer à Python que le chemin est de type
'Raw String' en préfixant le chemin avec la lettre 'r'"""
chemin = r'C:\PythonEnUneHeure\fichier_a_lire.txt'
"""La troisième méthode consiste à inverser le sens des slash"""
chemin = 'C:/PythonEnUneHeure/fichier_a_lire.txt'
