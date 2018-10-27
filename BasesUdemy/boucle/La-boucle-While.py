# La boucle While execute un bloc de code tant que la condition est verifiee

# Cette boucle While affichera les nombres de 0 a 9
i = 0
while i < 10:
	print(i)
	i += 1

# ATTENTION! Une boucle While est dangereuse
# Si on ne modifie pas la condition, on cree une boucle infinie.

while True:
	print('Cette boucle ne se termine jamais.')

# Il faut toujours permettre a la condition de changer
# afin de pouvoir sortir de la boucle.
