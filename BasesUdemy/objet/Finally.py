numerateur = 10
denominateur = 0

resultat = 0

try:
	resultat = numerateur / denominateur
except ZeroDivisionError:
	print('Division par zero impossible')
except TypeError:
	print('Une des deux variable nest pas un nombre')
except NameError as erreur:
	if 'numerateur' in erreur.message:
		print('La variable numerateur na pas ete declare')
	elif 'denominateur' in erreur.message:
		print('La variable denominateur na pas ete declare')
finally:
	# Bloc de code execute peu importe si l'operation est un succes ou non.
	print(resultat)