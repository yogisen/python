# 1er cas

# On attend de l'utilistaeur qu'il entre un nombre
# Mais l'utilisateur rentre malencontreusement un char
nombre = int(input("Veuillez entrer un nombre : "))
print(nombre)

# 2ème cas

# On attend toujours de l'utilisateur qu'il entre un nombre
# On prend en compte avec un try except
try:
  nombre = int(input("Veuillez entrer un nombre : "))
except ValueError:
  print("Vous n'avez pas entrer le bon type de donnée")

# 3ème cas

# On attend toujours de l'utilisateur qu'il entre un nombre
# On prend en compte avec une boucle while qui boucle tant que l'utilisateur n'a pas entré un nombre
nombre = input("Veuillez entrer un nombre : ")
while nombre.isdigit() is False:
  nombre = input("Veuillez entrer un nombre : ")
nombre = int(nombre)