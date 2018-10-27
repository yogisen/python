
# coding: utf-8

# ### definition

# In[2]:


liste_de_nombres = [1, 2, 3, 7, 8, 9]
liste_mixe = ['Pierre', 2, 'Paul', 3.5]
listes_imbriques = [1, 2, [3, 4]]


# #### compter les elements d'une liste

# In[4]:


longueur = len(liste_de_nombres)
print(longueur)


# ### Compter le nombre d'occurence d'une valeur dans une liste
# 

# In[7]:


liste_employes = ['Paul', 'Pierre', 'Paul', 'Kevin']
pauls = liste_employes.count('Paul')
print(pauls)


# ### ajouter

# In[8]:


liste = ['Pierre', 'Paul']

# Rajoute l'élément à la fin de la liste
liste.append('Jacques')

# Insérer un élément à une position définie dans la liste
liste.insert(1, 'Kevin')

# Fusionne la liste ajoutée à la liste existante
liste.extend(['Bertrand', 'John'])


# ### retirer

# In[10]:


liste = ['Pierre', 'Paul']

# Enlève l'élément 'Pierre'
liste.remove('Pierre')

# Enlève l'élément situé à l'indice 1
# Et retourne l'élément supprimé dans la variable element_enleve (ici: 'Paul')
element_enleve = liste.pop(2)

# Enlève l'élément situé à l'indice 0 (ici: 'Pierre')
del liste[0]


# ### trouver elements

# In[13]:


liste_employes = ['Pierre', 'Paul', 'Jacques']

if 'Pierre' in liste_employes:
	print('Un de vos employe se nomme Pierre')


# ### iterations

# In[14]:


liste_employes = ['Pierre', 'Paul', 'Jacques']

for nom in liste_employes:
	print(nom)


# In[19]:


liste_employes = ['Pierre', 'Paul', 'Jacques']

for nom in liste_employes:
	print('le noms ={0}'.format (nom))


# In[20]:


### trier


# In[21]:


liste = [1, 4, 6, 5, 2, 6, 8]

# Trier une liste
liste.sort() # Agit directement sur la liste
liste_en_ordre = sorted(liste) # La liste d'origine reste inchangée

# Trier une liste en sens inverse
liste.reverse()
liste.sort(reverse=True)
sorted(liste, reverse=True) # La liste d'origine reste inchangée


# In[22]:


#### modifier une liste


# In[24]:


liste = ['Pierre', 'Paul']

liste[0] = 'John'
print(liste)


# In[25]:


#### comprehension


# In[26]:


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

