from random import randint

nombre_a_deviner = randint(1, 100)
print(nombre_a_deviner)

premier_essai = input('Entrez un nombre (1er essai): ')

resultat = premier_essai == nombre_a_deviner

print(resultat)