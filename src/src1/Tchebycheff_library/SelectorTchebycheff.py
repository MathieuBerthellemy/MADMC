from src1.Tchebycheff_library.Opt import *
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
		ideal, nadir = self._get_ideal_nadir()

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
				- id de l'alternative la plus proche du point ideal en suivant la direcion d'optimisation

			Utilisation de la norme de Tchebycheff augmentee
		"""
		output = None
		best_val = 99999

		for key, value in self.table.get_available_rows(self.bounds).items():
			val = self._s(value, x0, omega, epsilon)
			if val < best_val:
				output = key
				best_val = val

		return output



	def _get_ideal_nadir(self):
		"""
			Output:
				- point ideal, point Nadir
		"""
		ideal = self.table.get_extremum_ideal();
		nadir = self.table.get_extremum_nadir();
		
		for key, value in self.table.get_available_rows(self.bounds).items():
		
			for i in range(len(self.bounds)):
			
				if self.table.direction[i] == Opt.MIN:
					nadir[i] = max(nadir[i], value[i]);
					ideal[i] = min(ideal[i], value[i]);

				if self.table.direction[i] == Opt.MAX:
					nadir[i] = min(nadir[i], value[i]);
					ideal[i] = max(ideal[i], value[i]);
				
		
		return ideal, nadir;
		


		