# AND sera execute avant OR

# Exemple sans parentheses
# Resultat sera True
resultat = False and False or True

# Exemple avec parentheses
# Resultat sera False
resultat = False and (False or True)

# Les parentheses permettent donc de changer l'ordre
# d'execution et donc le resultat