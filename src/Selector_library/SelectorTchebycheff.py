
class SelectorTchebycheff:
	"""
		Attributes:
			- table, AlternativesTable

		Public methods:
	"""

	def __init__(self, table):
		self.table = table
		self.table.reset_bounds()

	def reset_bounds(self):
		"""
			Reinitialise les bornes
		"""
		self.table.reset_bounds()

	def get_balanced_solution(self):
		"""
			retoune la solution la plus equilibree, (dans les bornes definie)
		"""
		ideal, nadir = self.table.get_ideal_nadir()

		alpha = 1/float(len(self.table.header))
		omega = [alpha/abs(x - y) if abs(x - y) != 0 else 0 for x, y in zip(nadir, ideal)]
		epsilon = 0.0001

		return self._get_solution_tchebycheff_augmentee(ideal, omega, epsilon)

	def cut(self, critere, value):
		"""
			coupe l'espace des solution (definie les bornes)
		"""
		self.table.set_bounds(critere, value)

	def _s(self, x, x0, omega, epsilon):
		"""
			distance de Tchebycheff
			s(x, x0, w) = max{wi|xi - x0|} + e*sum(wi|xi - x0|)
		"""
		tmp = [abs(i - j)*w for i, j, w in zip(x, x0, omega)]
		return max(tmp) + epsilon*sum(tmp)

	def _get_solution_tchebycheff_augmentee(self, x0, omega, epsilon):
		"""
			Inputs:
				- x0: point de reference
				- omega: direction d'optimisation
				- epsilon: facteur d'approximation

			Output:
				- id de l'alternative la plus proche du point ideal en suivant la direcion d'optimisation

			Utilisation de la norme de Tchebycheff augmentee
		"""
		output = None
		best_val = 99999

		for key, value in self.table.get_rows().items():
			val = self._s(value, x0, omega, epsilon)
			if val < best_val:
				output = key
				best_val = val

		return output



		


		