from random import randint

nombre_a_deviner = randint(1, 500)

nombre_essais = range(10)
for i in nombre_essais:

	essai = input('Entrez un nombre ({0} essai): '.format(i + 1))

	if essai < nombre_a_deviner:
		print('Le nombre a deviner est plus grand que {0}'.format(essai))
	elif essai > nombre_a_deviner:
		print('Le nombre a deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i + 1))
		break

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')