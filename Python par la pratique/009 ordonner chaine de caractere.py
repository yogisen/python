chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)