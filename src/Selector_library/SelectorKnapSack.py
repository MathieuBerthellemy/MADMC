from PL_knap_sack import get_knap_sack

class SelectorKnapSack:
	"""
		ATTRIBUTES:
			- table
	"""

	def __init__(self, table):
		self.table = table

	def get_solution(self, column_poids):
		sack = get_knap_sack(self.table, column_poids)
		return sack

	def cut(self, critere, bound):
		self.table.bounds[critere] = bound

	def reset_bounds(self):
		self.table.reset_bounds()

	




