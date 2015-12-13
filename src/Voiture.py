class Voiture:
	"""
		Attributs:
			- nom
			- puissance: MAX
			- couple: MAX
			- poids: MIN
			- acceleration: MIN
			- prix: MIN
			- pollution: MIN
	"""

	def __init__(self, nom, puissance, couple, poids, acceleration, prix, pollution):
		self.nom = nom
		self.puissance = puissance
		self.couple = couple
		self.poids = poids

		s, ms = acceleration.split('"')
		self.acceleration = (s, ms)

		self.prix = prix
		self.pollution = pollution

	def format_puissance(self):
		return self.puissance+"ch"

	def format_couple(self):
		return self.couple+"nm"

	def format_poids(self):
		return self.poids+"Kg"

	def format_acceleration(self):
		return self.acceleration[0]+ '"'+ self.acceleration[1]

	def format_prix(self):
		return self.prix+"€"

	def format_pollution(self):
		return self.pollution+"g/km"

	def vectorize(self):
		return (self.puissance, self.couple, self.poids, self.acceleration, self.prix, self.pollution)
