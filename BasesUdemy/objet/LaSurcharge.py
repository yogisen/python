class Employe():
	def __init__(self):
		self.salaireHoraire = 20

	def printSalaire(self):
		print('Le salaire de base est de {0}$/h'.format(self.salaireHoraire))

class Ingenieur(Employe):
	def __init__(self, prenom):
		Employe.__init__(self)
		self.prenom = prenom
		self.salaireHoraire = 25

	def printSalaire(self):
		print('Le salaire de base d\'un ingenieur est de {1}$/h'.format(self.prenom, self.salaireHoraire))

julie = Ingenieur('Julie')
julie.printSalaire()
tom = Employe()
tom.printSalaire()
