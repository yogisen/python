def affiche_tableau(tableau):

    print('   |   |')
    print(' ' + tableau[7] + ' | ' + tableau[8] + ' | ' + tableau[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tableau[4] + ' | ' + tableau[5] + ' | ' + tableau[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tableau[1] + ' | ' + tableau[2] + ' | ' + tableau[3])
    print('   |   |')


def pion_joueur():
    marque = ''
    while not (marque == 'X' or marque == 'O'):
        marque = input('Joueur 1: Est-ce que vous voulez jouer X ou O ?').upper()

    if marque == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def placer_marque(tableau, marque, position):
    tableau[position] = marque


def vérifie_gagnant(tableau, marque):
    return ((tableau[7] == marque and tableau[8] == marque and tableau[9] == marque) or  # ligne du haut
            (tableau[4] == marque and tableau[5] == marque and tableau[6] == marque) or  # ligne du milieu
            (tableau[1] == marque and tableau[2] == marque and tableau[3] == marque) or  # ligne du bas
            (tableau[7] == marque and tableau[4] == marque and tableau[1] == marque) or  # colonne de gauche
            (tableau[8] == marque and tableau[5] == marque and tableau[2] == marque) or  # colonne du milieu
            (tableau[9] == marque and tableau[6] == marque and tableau[3] == marque) or  # colonne de droite
            (tableau[7] == marque and tableau[5] == marque and tableau[3] == marque) or  # diagonale
            (tableau[9] == marque and tableau[5] == marque and tableau[1] == marque))  # diagonale

import random
def choix_premier():
    if random.randint(0, 1) == 0:
        return 'Joueur 2'
    else:
        return 'Joueur 1'


def vérifie_position(tableau, position):
    return tableau[position] == ' '

def vérifie_tableau_complet(tableau):
    for i in range(1,10):
        if vérifie_position(tableau, i):
            return False
    return True

def choix_du_joueur(tableau, joueur):
    # On a lu une chaine
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not vérifie_position(tableau, int(position)):
        position = input(joueur + ', choisissez la position où vous voulez jouer : (1-9) ')
    return int(position)


def rejouer():
    return input('Est-ce que vous voulez jouer à nouveau ? Répondez par Oui ou par Non : ').lower().startswith('o')


def tour_de_jeu(joueur, marque_joueur):
    jeu_en_cours = True

    affiche_tableau(leTableau)
    position = choix_du_joueur(leTableau, joueur)
    placer_marque(leTableau, marque_joueur, position)

    if vérifie_gagnant(leTableau, marque_joueur):
        affiche_tableau(leTableau)
        print('Bravo ' + joueur + ' ! Vous avez gagné !')
        jeu_en_cours = False
    else:
        if vérifie_tableau_complet(leTableau):
            affiche_tableau(leTableau)
            print('Match nul !')
            jeu_en_cours = False

    return jeu_en_cours


print('Bienvenue dans le jeu de Morpion !')

while True:
    # Préparer le tableau
    leTableau = [' '] * 10
    marque_joueur1, marque_joueur2 = pion_joueur()
    tour = choix_premier()
    print(tour + ' va commencer.')
    jeu_en_cours = True

    while jeu_en_cours:
        jeu_en_cours = tour_de_jeu("Joueur 1", marque_joueur1)
        if jeu_en_cours:
            jeu_en_cours = tour_de_jeu("Joueur 2", marque_joueur2)

    if not rejouer():
        break