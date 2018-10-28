numerateur = 10
denominateur = 0

# On essaie de calculer le resultat de l'operation.
# La division par zero etant impossible, Python va retourner une erreur.
# Avec le try on evite au programme de planter et on continue avec le print du bloc except.
try:
	resultat = numerateur / denominateur
	print(resultat)
except:
	print('Il y a un probleme avec cette operation.')
