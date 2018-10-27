continuer = 'o'
# On créé une liste de films vide qui va contenir les films ajoutés
liste_de_films = []

# Boucle principale
while continuer == 'o':
	# On récupère le nom du film à ajouter
	film_a_ajouter = raw_input('Entrez un titre de film a ajouter: ')
	# On créé une liste qui contient tous les films ajoutés en minuscule
	liste_minuscule = [film.lower() for film in liste_de_films]
	# On vérifie que le film ajouté n'est pas déjà présent dans la liste
	if film_a_ajouter.lower() in liste_minuscule:
		print('{0} est deja present dans la liste'.format(film_a_ajouter))
	else:
		# Si le film n'est pas déjà présent dans la liste, on l'ajoute
		liste_de_films.append(film_a_ajouter)

	# On demande si l'utilisateur veut ajouter un autre film
	continuer = raw_input('Voulez-vous ajouter un autre film? o/n ')
	print('')

# On trie la liste et on l'affiche à l'écran
liste_de_films.sort()
print(liste_de_films)
