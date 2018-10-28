class Employe(object):
	def __init__(self):
		self.salaireHoraire = 20

class Ingenieur(Employe):
	def __init__(self, prenom):
		super(Ingenieur, self).__init__()
		self.prenom = prenom

julie = Ingenieur('Julie')
print(julie.salaireHoraire)
