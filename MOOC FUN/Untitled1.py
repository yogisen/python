
# coding: utf-8

# In[7]:


# Pour convertir une variable d'un type
# a un autre, on peut utiliser les fonctions
# str(), int() et float()

# Variable de type string
mon_nom = 'Yogi'
# Variable de type integer
mon_age = 35

# On convertie la variable de type integer en string afin
# de pouvoir la concatener avec les autres variables.
print("Je m'appelle " + mon_nom + " et j'ai " + str(mon_age) + " ans.")
print (mon_nom)
print (mon_age)


# ### multiplication

# In[8]:


continuer = 0

while continuer == 0 :

	nombre = raw_input('Entrez un nombre: ')

	for i in range(1, 11):
		print('{0} x {1} = {2}'.format(i, nombre, int(nombre) * i))

	continuer = raw_input('Voulez-vous continuer? o/n ')

print('Fin du script.')


# In[9]:


from random import randint

nombre_a_deviner = randint(1, 500)

nombre_essais = range(10)
for i in nombre_essais:

	essai = input('Entrez un nombre ({0} essai): '.format(i + 1))

	if essai < nombre_a_deviner:
		print('Le nombre a deviner est plus grand que {0}'.format(essai))
	elif essai > nombre_a_deviner:
		print('Le nombre a deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i + 1))
		break

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')


# In[10]:


from random import randint

range = input('Entrez la difficulté 1-10/100/100/1000/...')
range = int(range)


while range <= 0 or range > 1000:

        if range >= 0:
                print ('le nombre doit etre positif')
        elif range > 1000:
                ('le nombre est trop grand')
                

        range = input('Entrez la difficulté 1-10/100/100/1000/...')
        range = int(range)
        
        
        


range = int(range)
nombre_a_deviner = randint(1, range)



nombre_essais = input('Combien voulez vous d essais')
nombre_essais = int(nombre_essais)
while nombre_essais < 1:
        nombre_essais = input('merci d indiquer un nombre positif')



        
i = 0
while i < nombre_essais:

	essai = input('Entrez un nombre ({0} essai): '.format(i + 1))
	essai = int(essai)

	if essai < nombre_a_deviner:
		print('Le nombre a deviner est plus grand que {0}'.format(essai))
	elif essai > nombre_a_deviner:
		print('Le nombre a deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i + 1))
		break

	i += 1

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')


# In[11]:


# La boucle For permet d'iterer a travers differents types de variables

# Cette boucle For affichera chaque lettre du mot bonjour
for lettre in 'Bonjour':
	print(lettre)

# Cette boucle For affichera chaque element de la liste
for i in [1, 2, 3, 4]:
	print(i)

# Pour creer rapidement une liste de nombres, on utilise la fonction range()
# range(5) = [0, 1, 2, 3, 4]

# Cette boucle affichera 0, 1, 2, 3 et 4
for i in range(5):
	print(i)


# In[ ]:


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


# In[12]:


# Permet de verifier plusieurs conditions a la suite

a = 5
b = 10

if a < b:
	print('a est plus petit que b')
elif a > b:
	print('a est plus grand que b')
else:
	print("a n'est ni plus grand, ni plus petit que b")
	print("a est donc forcement egal a b")


# In[13]:


# AND sera execute avant OR

# Exemple sans parentheses
# Resultat sera True
resultat = False and False or True

# Exemple avec parentheses
# Resultat sera False
resultat = False and (False or True)

# Les parentheses permettent donc de changer l'ordre
# d'execution et donc le resultat


# In[14]:


# Retourne True si les deux propositions sont vraies
# Si au moins une des proposition est fausse, retourne False.

# Retourne False
a = True and False

# Retourne False
b = False and True

# Retourne False
c = False and False

# Retourne True
d = True and True

print(a, b, c, d)


# In[15]:


# Retourne l'inverse de la proposition

# Retourne False
a = not True

# Retourne True
b = not False

print(a, b)


# In[5]:


# Retourne True si au moins une des proposition est vraie

# Retourne True
a = True or False

# Retourne True
b = False or True

# Retourne True
c = True or True

# Retourne False
d = False or False

print(a, b, c, d)


# In[6]:


from random import randint

range = input('Entrez la difficulté 1-10/100/100/1000/...')
range = int(range)
      
while true:
        if range <0:
                print('le nombre doit etre positif')
        else range > 1000:
                print('le nombre est trop grand')  
        
range = int(range)
nombre_a_deviner = randint(1, range)
nombre_essais = input('Combien voulez vous d essais')
nombre_essais = int(nombre_essais)
while nombre_essais < 1:
        nombre_essais = input('merci d indiquer un nombre positif')
        
i = 0
while i < nombre_essais:

	essai = input('Entrez un nombre ({0} essai): '.format(i + 1))
	essai = int(essai)

	if essai < nombre_a_deviner:
		print('Le nombre a deviner est plus grand que {0}'.format(essai))
	elif essai > nombre_a_deviner:
		print('Le nombre a deviner est plus petit que {0}'.format(essai))
	elif essai == nombre_a_deviner:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i + 1))
		break

	i += 1

if essai != nombre_a_deviner:
	print('Vous avez perdu')
	print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu.')

