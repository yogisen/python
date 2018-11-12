"""
On peut récupérer des informations entrées au clavier par
l'utilisateur avec la fonction input. On indique entre
parenthèses la phrase qui sera affichée à l'utilisateur.
"""
age = input('Quel age avez-vous ? ')

"""
Avec le module 'os', on a accès à plein de méthodes qui nous
permettent d'effectuer des opérations en lien avec notre système
d'exploitation, comme vérifier si un dossier existe. Pour pouvoir
utiliser le module os, il faut tout d'abord l'importer.
Pour importer un module on utilise le mot 'import' et le nom du module
comme ci-dessous :
"""
import os

# Une fois le module importé, nous pouvons utiliser les méthodes qu'il contient
# La fonction isdir pour vérifier si un dossier existe.
dossier_existe = os.path.isdir('C:/dossier_sur_disque')
print(dossier_existe)
# >>> True si le dossier existe, False s'il n'existe pas.

# Pour vérifier si un fichier existe on utilisera 'isfile'
fichier_existe = os.path.isfile('C:/dossier_sur_disque/fichier_sur_disque.txt')
print(fichier_existe)
# >>> True si le fichier existe, False s'il n'existe pas.

# Quelques méthodes intéressantes du module os
# Pour créer un dossier
os.makedirs('C:/dossier_sur_disque/sous_dossier')
# Pour supprimer un fichier
os.remove('C:/dossier_sur_disque/fichier_sur_disque.txt')
# Pour renommer un fichier
os.rename('C:/ancien_fichier.txt', 'C:/nouveau_fichier.txt')



