
from Tchebycheff_library.Opt import *

class SelectorTchebycheff:
	"""
		Attributes:
			- table, AlternativesTable
			- bounds, list

		Public methods:
	"""

	def __init__(self, table):
		self.table = table
		self.reset_bounds()


	def reset_bounds(self):
		self.bounds = self.table.get_extremum_ideal()

	def get_balanced_solution(self):
		nadir = self._get_nadir()
		ideal = self._get_ideal()

		omega = [x - y for x, y in zip(nadir, ideal)]
		epsilon = 0.0001

		return self._get_solution_tchebycheff_augmentee(ideal, omega, epsilon)

	def cut(self, critere, value):
		self.bounds[critere] = value

	def _s(self, x, x0, omega, epsilon):
		"""
			s(x, x0, w) = max{wi|xi - x0|} + e*(wi|xi - x0|)
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
				- id de l'alternative la plus proche du point idéal en suivant la direcion d'optimisation

			Utilisation de la norme de Tchebycheff augmentée
		"""
		output = None
		best_val = 99999

		for key, value in self.table.get_available_rows(self.bounds).items():
			val = self._s(value, x0, omega, epsilon)
			if val < best_val:
				output = key
				best_val = val

		return output



	def _get_nadir(self):
		"""
			Output:
				- point Nadir
		"""

		output = self.table.get_extremum_nadir();
		
		for key, value in self.table.get_available_rows(self.bounds).items():
		
			for i in range(len(output)):
			
				if self.table.direction[i] == Opt.MIN:
					output[i] = max(output[i], value[i]);

				if self.table.direction[i] == Opt.MAX:
					output[i] = min(output[i], value[i]);
				
		
		return output;
		

	def _get_ideal(self):
		"""
			Output:
				- point ideal
		"""

		output = self.table.get_extremum_ideal();
		
		for key, value in self.table.get_available_rows(self.bounds).items():
		
			for i in range(len(output)):
			
				if self.table.direction[i] == Opt.MIN:
					output[i] = min(output[i], value[i]);

				if self.table.direction[i] == Opt.MAX:
					output[i] = max(output[i], value[i]);
		
		return output;

		