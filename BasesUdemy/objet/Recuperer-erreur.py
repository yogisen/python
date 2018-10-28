#numerateur = 10
denominateur = 0


try:
	resultat = numerateur / denominateur
	print(resultat)
except ZeroDivisionError:
	print('Division par zero impossible')
except TypeError:
	print('Une des deux variable nest pas un nombre')
except NameError as erreur: # On recupere l'erreur dans la variable erreur
	if 'numerateur' in erreur.message:
		print('La variable numerateur na pas ete declare')
	elif 'denominateur' in erreur.message:
		print('La variable denominateur na pas ete declare')

