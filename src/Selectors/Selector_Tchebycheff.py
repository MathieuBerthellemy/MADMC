class Selector_Tchebycheff:
	"""
		Attributes:
			- data[]

		Public methods:
			- get_balanced_solution() 
			- (data, critere, value, orientation)
			- undo()
			- data_is_empty()
	"""

	def __init__(self, data):
		self.all_data = []
		self.all_data.append(data)

	def get_balanced_solution(self):
		nadir = self._get_nadir()
		ideal = self._get_ideal()

		omega = [x - y for x, y in zip(nadir, ideal)]
		epsilon = 0.01

		return self._get_solution_tchebycheff_augmentee(ideal, omega, epsilon)

	def cut(self, data, critere, value, orientation):
		new_data = []
		for v in self._get_last_data():
			vector = v.vectorize()
			if (orientation == "max" and vector[critere-1] > value) or (orientation == "min" and vector[critere-1] < value):
				new_data.append(v)
		self.all_data.append(new_data)

	def undo(self):
		self.all_data.pop()

	def data_is_empty(self):
		return (len(self._get_last_data()) == 0)
	




	def _get_last_data(self):
		return self.all_data[-1]

	def _s(self, x, x0, omega, epsilon):
		"""
			s(x, x0, w) = max{|xi - x0|} + e*|xi - x0|
		"""
		tmp = [abs(i - j) for i, j in zip(x, x0)]
		return max(tmp) + epsilon*sum(tmp)

	def _get_solution_tchebycheff_augmentee(self, x0, omega, epsilon):
		"""
			Inputs:
				- x: la liste des voitures
				- x0: point de reference
				- omega: direction d'optimisation
				- epsilon: facteur d'approximation

			Output:
				- voiture la plus proche du point idéal en suivant la direcion d'optimisation

			Utilisation de la norme de Tchebycheff augmentée
		"""
		output = None
		best_val = 99999

		for v in self._get_last_data():
			val = self._s(v.vectorize(), x0, omega, epsilon)
			if val < best_val:
				output = v
				best_val = val

		return output


	def _get_nadir(self):
		"""
			Inputs:
				- data: liste de voitures
			Output:
				- point Nadir
		"""

		tmp = [v.vectorize() for v in self._get_last_data()]

		n_puissance = min((t[0] for t in tmp))
		n_couple = min((t[1] for t in tmp))
		n_poids = max((t[2] for t in tmp))
		n_acceleration = max((t[3] for t in tmp))
		n_prix = max((t[4] for t in tmp))
		n_pollution = max((t[5] for t in tmp))

		return [n_puissance, n_couple, n_poids, n_acceleration, n_prix, n_pollution]
		

	def _get_ideal(self):
		"""
			Inputs:
				- data: liste de voitures
			Output:
				- point idéal
		"""

		tmp = [v.vectorize() for v in self._get_last_data()]

		i_puissance = max((t[0] for t in tmp))
		i_couple = max((t[1] for t in tmp))
		i_poids = min((t[2] for t in tmp))
		i_acceleration = min((t[3] for t in tmp))
		i_prix = min((t[4] for t in tmp))
		i_pollution = min((t[5] for t in tmp))

		return [i_puissance, i_couple, i_poids, i_acceleration, i_prix, i_pollution]


		