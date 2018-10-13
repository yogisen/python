from random import randint

nombre_a_deviner = randint(1, 100)
print(nombre_a_deviner)

premier_essai = input('Entrez un nombre (1er essai): ')

if premier_essai == nombre_a_deviner:
	print('Bravo, vous avez gagne')
elif premier_essai < nombre_a_deviner:
	print('Le nombre a deviner est plus grand que ' + str(premier_essai))
else:
	print('Le nombre a deviner est plus petit que ' + str(premier_essai))

print('Fin du jeu.')