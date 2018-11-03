
# 07 type

prenom = "Yogi"

if type(prenom) == str:
    print("La variable est une chaîne de caractères")

prenom = 0

if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")

# 008 - Remplacer un mot par un autre - Solution

phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
print(nouvelle_phrase)

# 009 - Ordonner une chaîne de caractère - Solution

chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)

# 013 - Créer une liste de nombres pairs de 1 à 100 - Solution
#On peut spécifier un écart à la fonction range en passant un nombre en troisième argument.

liste_nombre_pairs = range(2, 101, 2)
print(list(liste_nombre_pairs))

