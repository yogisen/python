# 015 - Compter le nombre d'occurrences d'une lettre dans une phrase - Solution

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
print(phrase.lower().count(lettre_a_chercher))

# 017 - Récupérer des éléments dans une liste -

ma_liste = ["Pierre", "Paul", "Marie"]

print(ma_liste[0]) # Pierre
print(ma_liste[-1]) #Marie
print(ma_liste[:2])  # ['Pierre', 'Paul']
print(ma_liste[-2:]) # ['Paul', 'Marie']


#018 - Récupérer un élément sur deux dans une liste

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[::2])

# 020 - Récupérer les éléments communs à deux listes

liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
s1 = set(liste_01)
s2 = set(liste_02)

print (s1.intersection(s2))