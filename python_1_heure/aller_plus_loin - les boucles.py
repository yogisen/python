"""
Une boucle sert à itérer à travers une structure de donnée.
On peut par exemple itérer à travers une chaîne de caractères
pour les afficher un à un
"""
prenom = 'Pierre'
for lettre in prenom:
	print(lettre)

"""La variable lettre va être égal à chaque lettre de la
variable prenom définie ci-dessus. On peut utiliser n'importe
quel nom de variable (on aurait pu utiliser 'l' au lieu de 'lettre'"""
for l in prenom:
	print(l)

"""On peut utiliser une boucle pour accéder à chaque élément d'une liste"""
ma_liste = ['Pierre', 'Paul', 'Jacques']
for prenom in ma_liste:
	print(prenom)

"""On peut également utiliser une boucle pour répéter une action
un certain nombre de fois. On va pour cela utiliser la fonction
range qui permet de créer une liste à la volée. La boucle
ci-dessous va printer les nombres de 0 à 9."""
for i in range(10):
	print(i)

"""Il existe un autre type de boucle, qui est la boucle while.
La boucle while va continuer de s'exécuter tant que la condition
que l'on définie est vraie. Les boucles while sont donc 'dangereuses'
car elles permettent de créer des boucles infinies (des boucles
qui ne se terminent jamais et qui vont donc faire planter notre programme)."""
while True:
	print('Ceci est une boucle infinie !')

"""Avec une boucle while il faut donc s'assurer que la condition
peut devenir fausse comme dans l'exemple ci-dessous. On va passer
10 fois dans la boucle, jusqu'à ce que i soit plus grand que 10."""
i = 1
while i < 10:
	print('i est plus petit que 10')
	i += 1  # Façon rapide d'incrémenter i. Similaire à : i = i + 1

