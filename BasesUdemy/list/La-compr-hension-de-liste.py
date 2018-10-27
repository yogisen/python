liste = [1, 2, 3, 4, 5]
liste_multipliee_par_deux = []

# On itère à travers la liste et on ajoute à la nouvelle liste
# les valeurs de la première, multiplié par 2.
for i in liste:
	liste_multipliee_par_deux.append(i * 2)

print(liste)
print(liste_multipliee_par_deux)


# La façon en 'Compréhension de liste'
liste = [i*2 for i in liste]
print(liste)

# Avec un if
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste = [i*2 for i in liste if i > 0]
print(liste)

# Avec un if else
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste = [i*2 if i > 0 else i for i in liste]
print(liste)
