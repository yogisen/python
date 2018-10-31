# definir une fonction devine ?
# A la moitié des essais demander l'aide d'un ami =
    # 1) chaine de caractere de la taille de nbAdeviner
    # 2) nbAdeviner/2 +3
    # 3) le nbre ecrit à l'envers
# aller voir la doc du input


from random import randint

print('bienvenue dans le jeu du nombre à deviner')
level = 0

while level != 10 and 100 and 1000:
    level = input('select your level : 10, 100, 1000')
    level = int(level)
# comment ne pas avoir a convertir un imput(google)

nb_a_deviner = randint(1,int(level))

nbre_de_chance = input ('nbr de chance ? ')
nbre_de_chance = int(nbre_de_chance)
# comment ne pas avoir a convertir un imput(google)

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
        if nb_a_deviner == votre_valeur:
            print('bravo')
        else:
            print ('give me more money')














