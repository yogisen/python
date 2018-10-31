from random import randint

print('bienvenue dans le jeu du nombre à deviner')
level = input('select your level : 10, 100, 1000')

nb_a_deviner = randint(1,int(level))

nbre_de_chance = input ('nbr de chance ? ')
nbre_de_chance = int(nbre_de_chance)
derniere_chance = 0
print('le nombre à deviner est ' + str(nb_a_deviner))

print('let s start')

i = 0
while i < nbre_de_chance:

    votre_valeur = input('Entrez un nombre ({0} essai): '.format(i + 1))
    votre_valeur = int(votre_valeur)

    if nb_a_deviner < votre_valeur:
        print('le nbre à deviner est plus petit')
    elif nb_a_deviner > votre_valeur:
        print(' plus grand')
    elif nb_a_deviner == votre_valeur:
        print('bravo')

    i += 1

if nb_a_deviner != votre_valeur:
    print('vous avez perdu')
    last_chance = input(' veux tu une chance supplementaire ?y/n ')

    if last_chance != 'y':
        print('à bientot')
    else:

        votre_valeur = input('derniere chance')
        votre_valeur = int(votre_valeur)
        nb_a_deviner == votre_valeur
        print('bravo')














