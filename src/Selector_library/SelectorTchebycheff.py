
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
		self.table.reset_bounds()

	def get_balanced_solution(self):

		ideal, nadir = self.table.get_ideal_nadir()

		omega = [x - y for x, y in zip(nadir, ideal)]
		epsilon = 0.0001

		return self._get_solution_tchebycheff_augmentee(ideal, omega, epsilon)

	def cut(self, critere, value):
		self.table.set_bounds(critere, value)

	def _s(self, x, x0, omega, epsilon):
		"""
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



		


		