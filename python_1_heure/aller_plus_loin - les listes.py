"""Dans cet exemple, nous avons écrit une liste à l'intérieur du fichier.
Une liste est une structure de donnée en Python qui permet de contenir
plusieurs éléments. Ici, nous créons une liste composée de deux integer,
d'une chaîne de caractère et d'un float (nombre à virgule)."""
ma_liste = ['Pierre', 2, 'bonjour', 2.345]

# Pour ajouter un élément dans une liste on utilise la méthode 'append'
ma_liste.append(5)
print(ma_liste)
# >>> ['Pierre', 2, 'bonjour', 2.345, 5]

# Pour enlever un élément d'une liste on utilise la méthode 'remove'
ma_liste.remove(5)
print(ma_liste)
# >>> ['Pierre', 2, 'bonjour', 2.345]

# Pour récupérer un élément d'une liste, on utilise la syntaxe suivante
print(ma_liste[0])
# >>> 'Pierre'

"""En programmation on commence à compter à 0. Le premier élément a
donc un index de 0. On peut aussi récupérer des éléments en commençant
par la fin. La ligne suivante va récupérer le dernier élément de la liste"""
print(ma_liste[-1])
print(ma_liste[-2])  # Récupère l'avant-dernier élément de la liste

"""On peut également récupérer plusieurs éléments grâce à ce qu'on appelle
les 'slices'. Avec la ligne suivante on va récupérer les 2 premiers éléments
de la liste"""
print(ma_liste[0:2])

# Pour créer facilement une liste de nombres, on peut utiliser la fonction range
ma_liste = range(5)
print(ma_liste)
# >>> [0, 1, 2, 3, 4]

ma_liste = range(10, 15)  # On créé une liste de 10 à 15 (15 exclu)
print(ma_liste)
# >>> [10, 11, 12, 13, 14]

ma_liste = range(10, 20, 2)  # De 10 à 20 avec un écart de 2
print(ma_liste)
# >>> [10, 12, 14, 16, 18]