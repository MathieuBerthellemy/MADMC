
class AlternativesTable:
	"""
		Attributes:
			- header, list<String>
			- direction, list<Bool>
			- rows, dictionary <ID_key, Tupple>
			
			- invalid_rows = Array<Integer>
			- columns_validity = list<Bool>
			- bounds
	"""

	def __init__(self, *data):
		self.header = []
		self.direction = [False]*len(data)
		self.rows = {}

		self.invalid_rows = []
		self.columns_validity = [True]*len(data)

		for col_name in data:
			self.header.append(col_name)

		self.reset_bounds()


	def reset_bounds(self):
		self.bounds = self.get_extremum_ideal()

	def set_bounds(self, col, bounds):
		self.bounds[col] = bounds

	def unset_row(self, key):
		self.invalid_rows.append(key)

	def unset_column(self, key):
		self.columns_validity[key] = False
		
	def set_row(self, key):
		try:
			self.invalid_rows.remove(key)
		except ValueError:
			pass # or scream: thing not in some_list!
		except AttributeError:
			pass # call security, some_list not quacking like a list!


	def set_column(self, key):
		self.columns_validity[key] = True


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
		self.bounds = self.get_extremum_ideal()

	def set_col_min(self, *col_numbers):
		for column in col_numbers:
			self.direction[column] = False
		self.bounds = self.get_extremum_ideal()



	def get_columns_count(self):
		return len(self.header)

	def get_rows_count(self):
		return len(self.rows)

	def get_extremum_nadir(self):
		output = [0]*len(self.header)
		size = len(self.header)
		
		for i in range(size):
			# MIN
			if self.direction[i] ==  False:
					output[i] = float("-inf");
			# MAX
			if self.direction[i] ==  True:
					output[i] = float("inf");

		return output

	def get_extremum_ideal(self):
		output = [0]*len(self.header)
		size = len(self.header)
		
		for i in range(size):
			# MIN
			if self.direction[i] ==  False:
					output[i] = float("inf");
			# MAX
			if self.direction[i] ==  True:
					output[i] = float("-inf");

		return output


	def get_ideal_nadir(self):
		"""
			Output:
				- point ideal, point Nadir
		"""
		ideal = self.get_extremum_ideal();
		nadir = self.get_extremum_nadir();

		for key, value in self.rows.items():
			if key not in self.invalid_rows:
				for i in range(len(self.header)):
					
					# MIN
					if self.direction[i] == False:
						nadir[i] = max(nadir[i], value[i]);
						ideal[i] = min(ideal[i], value[i]);

					# MAX
					if self.direction[i] == True:
						nadir[i] = min(nadir[i], value[i]);
						ideal[i] = max(ideal[i], value[i]);

		# # supprime toute les colonnes non prises en compte
		# indexes = sorted(list(self.invalid_columns), reverse=True)
		# for i in indexes:
		# 	nadir.pop(i)
		# 	ideal.pop(i)
					
		return ideal, nadir;





	def get_rows(self, bounded=True):
		"""
			return a dictionary filtred by invalid rows, invalid columns and bounds
		"""
		output = {}
		for key, value in self.rows.items():
			if key not in self.invalid_rows:
				# La ligne est-elle valide au sens des bornes
				valid = True
				for i in range(len(self.header)):
					if ((self.direction[i] == False and value[i] >= self.bounds[i]) or (self.direction[i] == True and value[i] <= self.bounds[i]) and bounded):
						valid = False

				if	valid:
					# new_row = []
					# for i in range(len(self.header)):
					# 	if i not in self.invalid_columns:
					# 		new_row.append(value[i])
					# output[key] = new_row
					output[key] = value

		
		return output
