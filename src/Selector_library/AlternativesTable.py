
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
		"""
			definit les colonnes donnees en parametre comme des colonnes de maximisation
		"""
		for column in col_numbers:
			self.direction[column] = True
		self.bounds = self.get_extremum_ideal()

	def set_col_min(self, *col_numbers):
		"""
			definit les colonnes donnees en parametre comme des colonnes de minimisation
		"""
		for column in col_numbers:
			self.direction[column] = False
		self.bounds = self.get_extremum_ideal()



	def get_columns_count(self):
		return len(self.header)

	def get_rows_count(self):
		return len(self.rows)

	def get_extremum_nadir(self):
		"""
			retourne les valeurs infinies pour chaque critere (-inf si min, inf si max)
		"""
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
		"""
			retourne les valeurs infinies pour chaque critere (-inf si max, inf si min)
		"""
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


	def get_EC(self, bounded):
		"""
			Retourne l'enveloppe convexe des donnees
		"""
		EC = [[] for i in range(len(self.header))]
		ideal = self.get_extremum_ideal()

		rows_set = self.get_rows(bounded)
		
		for key, value in rows_set.items():
			if key not in self.invalid_rows:
				for i in range(len(self.header)):
					# MIN
					if self.direction[i] == False:
						if value[i] < ideal[i]:
							ideal[i] = value[i]
							EC[i] = value	

					# MAX
					if self.direction[i] == True:
						if value[i] > ideal[i]:
							ideal[i] = value[i]
							EC[i] = value		

		return EC
						



	def get_ideal_nadir(self, bounded=True):
		"""
			Output:
				- point ideal, point Nadir approche
		"""
		ideal = self.get_extremum_ideal();
		nadir = self.get_extremum_nadir();

		# Enveloppe concave
		EC = self.get_EC(bounded)
		
		if len(EC[0]) > 0:
			for c in range(len(self.header)):
			
				# MIN
				if self.direction[c] == False:
					ideal[c] = min(ec[c] for ec in EC)
					nadir[c] = max(ec[c] for ec in EC)

				# MAX
				if self.direction[c] == True:
					ideal[c] = max(ec[c] for ec in EC)
					nadir[c] = min(ec[c] for ec in EC)

			# # supprime toute les colonnes non prises en compte
			# indexes = sorted(list(self.invalid_columns), reverse=True)
			# for i in indexes:
			# 	nadir.pop(i)
			# 	ideal.pop(i)

		print "ideal", ideal
		print "nadir", nadir
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
