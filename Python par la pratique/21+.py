# 022 - Récupérer une valeur dans un dictionnaire

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

# C'est ce principe que nous mettons en place ici.' \
# Nous récupérons la première clé et si celle-ci n'existe pas, nous retournons un dictionnaire vide :
# employes.get("01", {})
# sans risquer de faire planter le script.
# En effet, si nous ne retournions par de valeur par défaut et que la clé n'existe pas dans le dictionnaire, la 2e méthode get ne fonctionnerait pas car elle s'exécuterait sur None.
# Donc si la première clé n'est pas trouvée, le get va agir sur un dictionnaire vide et ainsi de suite, évitant tout risque d'erreur.


# 023 - Additionner les valeurs d'un dictionnaire - Solution

employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(sum(employes.values()))

# 024 - Trouver l'erreur de module - Solution

import random

nombre_aleatoire = random.randint(0, 5)
print(nombre_aleatoire)

# POINTS IMPORTANTS À RETENIR
# Pour utiliser une fonction à l'intérieur d'un module,
# il ne faut pas oublier de préfixer la fonction par le nom du module.
# Pour importer une fonction à l'intérieur d'un module
#  directement dans l'espace global de notre script,
#  on peut utiliser la syntaxe from module import fonction .