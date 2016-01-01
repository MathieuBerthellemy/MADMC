from PL_knap_sack import get_knap_sack

class SelectorKnapSack:
	"""
		ATTRIBUTES:
			- table
			- column_poids
			- bounds
	"""

	def __init__(self, table):
		self.table = table
		self.column_poids = 4
		self.bounds = table.get_extremum_ideal()

	def get_solution(self):
		sack = get_knap_sack(self.table, self.column_poids, self.bounds)
		return sack

	def cut(self, critere, bounds):
		self.bounds[critere] = bounds

	def reset_bounds(self):
		self.bounds = self.table.get_extremum_ideal()


	




