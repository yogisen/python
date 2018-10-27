dictionnaire = {'Pierre': 40, 'Paul': 25}

# Supprimer avec del
del dictionnaire['Pierre']

# Pop retourne la valeur associée à la clé
dictionnaire.pop('Pierre')
>>> 40

# Efface tout le contenu du dictionnaire.
dictionnaire.clear()