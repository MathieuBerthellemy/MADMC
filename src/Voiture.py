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
		self.puissance = int(puissance)
		self.couple = int(couple)
		self.poids = int(poids)

		s, ms = acceleration.split('"')
		self.acceleration = (int(s), int(ms))

		self.prix = int(prix)
		self.pollution = int(pollution)

	def format_puissance(self):
		return "".join([str(self.puissance), "ch"])

	def format_couple(self):
		return "".join([str(self.couple), "nm"])

	def format_poids(self):
		return "".join([str(self.poids), "Kg"])

	def format_acceleration(self):
		return "".join([str(self.acceleration[0]), '"', str(self.acceleration[1])])

	def get_float_acceleration(self):
		return self.acceleration[0]+self.acceleration[1]/10

	def format_prix(self):
		return "".join([str(self.prix), "€"])

	def format_pollution(self):
		return "".join([str(self.pollution), "g/km"])

	def vectorize(self):
		return [self.puissance, self.couple, self.poids, self.get_float_acceleration(), self.prix, self.pollution]

	def to_string(self):
		print(self.nom)
		print("1/ "+ self.format_puissance())
		print("2/ "+ self.format_couple())
		print("3/ "+ self.format_poids())
		print("4/ "+ self.format_acceleration())
		print("5/ "+ self.format_prix())
		print("6/ "+ self.format_pollution())


