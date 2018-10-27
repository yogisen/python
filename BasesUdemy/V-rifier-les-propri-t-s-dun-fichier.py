chemin = 'C:\Users\Thibh\Desktop\Udemy.txt'

f = open(chemin, 'r')

# Pour vérifier si un fichier est fermé
f.closed
>>> False

# Pour vérifier le mode dans lequel le fichier a été ouvert
f.mode
>>> 'r'

# Pour vérifier le chemin du fichier
f.name
>>> 'C:\Users\Thibh\Desktop\Udemy.txt'