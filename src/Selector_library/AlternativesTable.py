
class AlternativesTable:
	"""
		Attributes:
			- header, list<String>
			- direction, list<Bool>
			- rows, dictionary <ID_key, Tupple>
			
			- invalid_rows = Array<int>
			- invalid_columns = Array<int>
	"""

	def __init__(self, *data):
		self.header = []
		self.direction = [False for i in data]
		self.rows = {}

		self.invalid_rows = []
		self.invalid_columns = []

		for col_name in data:
			self.header.append(col_name)

		self.bounds = get_extremum_ideal()


	def set_bounds(self, col, bounds):
		self.bounds[col] = bounds

	def unset_rows(self, key):
		self.invalid_rows.append(key)

	def unset_column(self, key):
		self.invalid_columns.append(key)

	def set_rows(self, key):
		self.invalid_rows.remove(key)

	def set_column(self, key):
		self.invalid_columns.remove(key)


	def get_rows(self):
		"""
			return a dictionary filtred by invalid rows and invalid columns and bounds
		"""
		output = {}
		for key, value in self.rows.items():
			if key not in self.invalid_rows:
				row = []

				valid = True
				for i in range(len(self.header)):
					if i not in self.invalid_columns:	
						if (self.direction[i] == False and value[i] >= bounds[i]) or (self.direction[i] == True and value[i] <= bounds[i]):
							valid = False
				if	valid:
					output[key] = row

		return output


	

	def add_row(self, id_key, values):
		"""
			Input:
				values: this list of values to add

		"""
		if len(values) == len(self.header):
			self.rows[id_key] = values
		else:
			print("format doestn't match (add_row)")


	def set_col_max(self, *col_numbers):
		for column in col_numbers:
			self.direction[column] = True
		self.bounds = get_extremum_ideal()

	def set_col_min(self, *col_numbers):
		for column in col_numbers:
			self.direction[column] = False
		self.bounds = get_extremum_ideal()



	def get_columns_count(self):
		return len(self.header)

	def get_rows_count(self):
		return len(self.rows)

	def get_extremum_nadir(self):
		output = [0]*(len(self.header)-len(self.invalid_columns))
		size = len(self.header)
		
		for i in range(size):
			if i not in self.invalid_columns:
				# MIN
				if self.direction[i] ==  False:
						output[i] = -99999999;
				# MAX
				if self.direction[i] ==  True:
						output[i] = 99999999;

		return output

	def get_extremum_ideal(self):
		output = [0]*(len(self.header)-len(self.invalid_columns))
		size = len(self.header)
		
		for i in range(size):
			if i not in self.invalid_columns:
				# MIN
				if self.direction[i] ==  False:
						output[i] = 99999999;
				# MAX
				if self.direction[i] ==  True:
						output[i] = -99999999;

		return output



	def get_ideal_nadir(self):
		"""
			Output:
				- point ideal, point Nadir
		"""
		ideal = self.get_extremum_ideal();
		nadir = self.get_extremum_nadir();

		self.get_row(bounds)

		for key, value in self.get_rows().items():

			if key not in self.invalid_rows:
				for i in range(len(bounds)):
					if i not in self.invalid_columns:
						# MIN
						if self.direction[i] == False:
							nadir[i] = max(nadir[i], value[i]);
							ideal[i] = min(ideal[i], value[i]);

						# MAX
						if self.direction[i] == True:
							nadir[i] = min(nadir[i], value[i]);
							ideal[i] = max(ideal[i], value[i]);
					
		return ideal, nadir;