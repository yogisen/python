class Employe():
	def __init__(self):
		self.salaireHoraire = 20

class Ingenieur(Employe):
	def __init__(self, prenom):
		Employe.__init__(self)
		self.prenom = prenom

julie = Ingenieur('Julie')
print(isinstance(julie, Ingenieur))
print(isinstance(julie, Employe))

print(issubclass(Ingenieur, Employe))
print(issubclass(Employe, Ingenieur))