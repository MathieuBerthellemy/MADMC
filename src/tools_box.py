def get_balanced_solution(data):
	nadir = get_nadir(data)
	ideal = get_ideal(data)

	omega = [x - y for x, y in zip(nadir, ideal)]
	epsilon = 0.01

	return get_solution_tchebycheff_augmentee(data, ideal, omega, epsilon)


def s(x, x0, omega, epsilon):
	"""
		s(x, x0, w) = max{|xi - x0|} + e*|xi - x0|
	"""
	tmp = [abs(i - j) for i, j in zip(x, x0)]
	return max(tmp) + epsilon*sum(tmp)

def get_solution_tchebycheff_augmentee(data, x0, omega, epsilon):
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

	for v in data:
		val = s(v.vectorize(), x0, omega, epsilon)
		if val < best_val:
			output = v
			best_val = val

	return output


def get_nadir(data):
	"""
		Inputs:
			- data: liste de voitures
		Output:
			- point Nadir
	"""

	tmp = [v.vectorize() for v in data]

	n_puissance = min((t[0] for t in tmp))
	n_couple = min((t[1] for t in tmp))
	n_poids = max((t[2] for t in tmp))
	n_acceleration = max((t[3] for t in tmp))
	n_prix = max((t[4] for t in tmp))
	n_pollution = max((t[5] for t in tmp))

	return [n_puissance, n_couple, n_poids, n_acceleration, n_prix, n_pollution]
	

def get_ideal(data):
	"""
		Inputs:
			- data: liste de voitures
		Output:
			- point idéal
	"""

	tmp = [v.vectorize() for v in data]

	i_puissance = max((t[0] for t in tmp))
	i_couple = max((t[1] for t in tmp))
	i_poids = min((t[2] for t in tmp))
	i_acceleration = min((t[3] for t in tmp))
	i_prix = min((t[4] for t in tmp))
	i_pollution = min((t[5] for t in tmp))

	return [i_puissance, i_couple, i_poids, i_acceleration, i_prix, i_pollution]

