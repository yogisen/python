# Création d'un dictionnaire
dictionnaire = {'Pierre': 40, 'Paul': 25}

# Syntaxe pour accéder à la valeur correspondant à une clé
dictionnaire[clef]
>>> valeur

dictionnaire['Pierre']
>>> 40

dictionnaire = {'Pierre': {'age': 40, 'profession': 'banquier'}, 'Paul': {'age': 25, 'profession': 'ingenieur'}}
dictionnaire['Pierre']
>>> {'age': 40, 'profession': 'banquier'}
dictionnaire['Pierre']['age']
>>> 40
dictionnaire['Pierre']['profession']
>>> 'banquier'

# Avec get():
dictionnaire.get('Pierre')
>>> 40

dictionnaire.keys()
>>> ['Pierre', 'Paul']

dictionnaire.values()
>>> [40, 25]

# Items pour récupérer une liste de tuple dans le format (clé, valeur)
dictionnaire.items()
>>> [('Paul', 25), ('Pierre', 40)]
