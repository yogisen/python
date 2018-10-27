from random import randint

range = input('Entrez la difficulté 1-10/100/100/1000/...')
range = int(range)


while range <= 0 or range > 1000:

        if range >= 0:
                print ('le nombre doit etre positif')
        elif range > 1000:
                ('le nombre est trop grand')
                

        range = input('Entrez la difficulté 1-10/100/100/1000/...')
        range = int(range)
           
        
range = int(range)
nombre_a_deviner = randint(1, range)
nombre_essais = input('Combien voulez vous d essais')
nombre_essais = int(nombre_essais)
while nombre_essais < 1:
        nombre_essais = input('merci d indiquer un nombre positif')
        
i = 0
while i < nombre_essais:

	essai = input('Entrez un nombre ({0} essai): '.format(i + 1))
	essai = int(essai)

	if essai < nombre_a_deviner:
		print('Le nombre a deviner est plus grand que {0}'.format(essai))
	elif essai > nombre_a_deviner:
		print('Le nombre a deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i + 1))
		break

	i += 1

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')
