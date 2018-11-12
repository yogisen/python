"""Pour lire un fichier on utilise la syntaxe suivante"""
with open(chemin_fichier, 'r') as f:
	contenu_du_fichier = f.read()
	print(contenu_du_fichier)

"""Pour écrire dans un fichier on utilise la syntaxe suivante"""
with open(chemin_fichier, 'w') as f:
	f.write('Je mets du texte dans le fichier.')
