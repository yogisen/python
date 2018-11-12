# On défini le chemin du fichier à lire
chemin_fichier = r"C:\PythonEnUneHeure\fichier_a_lire.txt"

# Première façon de lire ou écrire dans un fichier.
# On utilise le mode 'r' pour lire le fichier.
fichier = open(chemin_fichier, 'r')
contenu_fichier = fichier.read()
# Ave cette façon, il ne faut pas oublier de fermer le fichier
fichier.close()
print(contenu_fichier)

# Deuxième façon de faire qui évite d'avoir à utiliser fichier.close()
# Le fichier sera automatiquement fermé.
# On utilise le mode 'w' pour écrire dans le fichier.
with open(chemin_fichier, 'w') as f:
	f.write('Mais en ete il peut faire jusqua')

# On importe le module json
import json
chemin_fichier = r"C:\PythonEnUneHeure\liste.json"

# On écrit une liste dans le fichier JSON
with open(chemin_fichier, 'w') as f:
	json.dump([1, 2, 3, 4, 5], f)

# On lit le contenu du fichier que l'on vient d'écrire
with open(chemin_fichier, 'r') as f:
	ma_liste = json.load(f)

# On rajoute une valeur à la liste récupérée
ma_liste.append(6)

# On écrit la liste avec la nouvelle valeur dans le fichier JSON.
with open(chemin_fichier, 'w') as f:
	json.dump(ma_liste, f)