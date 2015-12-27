from Tchebycheff_library.Opt import *

class AlternativesTable:
	"""
		Attributes:
			- header, list<String>
			- direction, list<Opt>
			- rows, dictionary <ID_key, Tupple>

		Public methods:
	"""

	def __init__(self, *data):
		self.header = []
		self.direction = []
		self.rows = {}
		
		for tup in data:
			self.header.append(tup[0])
			self.direction.append(tup[1])

	def add_row(self, id_key, values):
		"""
			Input:
				values: this list of values to add

		"""
		if len(values) == len(self.header):
			self.rows[id_key] = values
		else:
			print("format doestn't match (add_row)")

	
	
	def get_available_rows(self, bounds):
		"""
			Input:
				- bounds

			Output:
				- Dictionary
		"""
		output = {}

		size = len(self.header)
		for key, value in self.rows.items():

			available = True
			for i in range(size):
				if (self.direction[i] == Opt.MIN and value[i] >= bounds[i]) or (self.direction[i] == Opt.MAX and value[i] <= bounds[i]):
					available = False

			if available:
				output[key] = value
			
		return output

	def get_columns_count(self):
		return len(self.header)

	def get_rows_count(self):
		return len(self.rows)

	def get_extremum_nadir(self):
		output = [0 for column in self.header]
		size = len(self.header)
		
		for i in range(size):
			if self.direction[i] ==  Opt.MIN:
					output[i] = -99999999;
			if self.direction[i] ==  Opt.MAX:
					output[i] = 99999999;

		return output

	def get_extremum_ideal(self):
		output = [0 for column in self.header]
		size = len(self.header)
		
		for i in range(size):
			if self.direction[i] ==  Opt.MIN:
					output[i] = 99999999;
			if self.direction[i] ==  Opt.MAX:
					output[i] = -99999999;

		return output