class Interactor_human:
	def get_satisfait(self):
		return int(input("satisfait ? (0/1)")) == 1

	def get_critere(self):
		return int(input("critère à améliorer"))


