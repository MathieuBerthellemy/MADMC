from Selector_library.PL_max_regret import max_regret

class SelectorMinMaxRegret:
	"""
		ATTRIBUTES
			table: table des alternatives
			preferences: Array of tupples [(a, b), ...] a > b
	"""
	
	def __init__(self, table):
		self.table = table
		self.reset_preferences()

	def reset_preferences(self):
		self.preferences = []

	def get_solution(self):
		return self._minmax_regret()

	def add_preference(self, pref):
		"""
			INPUTS:
				pref: un tupple d'arite 2 (a, b) signifiant que le decideur prefere a a b
			OUTPUTS:
				/
		"""
		self.preferences.append(pref)


	def _minmax_regret(self):
		"""
			INPUTS: 
				/
			OUTPUTS:
				- argmin{a in A} max_regret(a): retourne l'alternative ayant le plus petit regret maximal
		"""
		best_row = None
		regret_minmax = 999999

		for key, r in self.table.rows.items():
			# appel au PL
			regret_max  = max_regret(r, self.table, self.preferences)
			print regret_max
			if regret_max < regret_minmax and regret_max != -1:
				best_row = key
				regret_minmax = regret_max

		#print regret_minmax

		return best_row
