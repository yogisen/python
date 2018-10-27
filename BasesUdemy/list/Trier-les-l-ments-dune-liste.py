liste = [1, 4, 6, 5, 2, 6, 8]

# Trier une liste
liste.sort() # Agit directement sur la liste
liste_en_ordre = sorted(liste) # La liste d'origine reste inchangée

# Trier une liste en sens inverse
liste.reverse()
liste.sort(reverse=True)
sorted(liste, reverse=True) # La liste d'origine reste inchangée