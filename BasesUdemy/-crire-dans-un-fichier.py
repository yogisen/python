chemin = 'C:\Users\Thibh\Desktop\Udemy.txt'

# Pour écrire dans un fichier et écraser son contenu
f = open(chemin, 'w')
f.write('Nouveau contenu')

# Pour écrire dans un fichier et rajouter du contenu à sa suite
f = open(chemin, 'a')
f.write('Contenu ajouté')
