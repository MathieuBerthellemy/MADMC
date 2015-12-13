
def get_solution_nadir_ideal(data, nadir, ideal):
	"""
		Inputs:
			- data: la liste des voitures
			- nadir: vecteur contenant la pire valeur sur chaque critère
			- ideal: vecteur contenant la meilleur valeur sur chaque critère

		Output:
			- voiture la plus proche du point idéal en direction du point Nadir

		Utilisation de la norme de Tchebycheff augmentée
	"""
	
	print("TODO")


def get_nadir(data):
	"""
		Inputs:
			- data: liste de voitures
		Output:
			- point Nadir
	"""

	n_puissance = min((v.puissance for v in data))
	n_couple = min((v.couple for v in data))
	n_poids = max((v.poids for v in data))
	n_acceleration = max((v.acceleration for v in data))
	n_prix = max((v.prix for v in data))
	n_pollution = max((v.pollution for v in data))

	return (n_puissance, n_couple, n_poids, n_acceleration, n_prix, n_pollution)
	

def get_ideal(data):
	"""
		Inputs:
			- data: liste de voitures
		Output:
			- point idéal
	"""

	i_puissance = max((v.puissance for v in data))
	i_couple = max((v.couple for v in data))
	i_poids = min((v.poids for v in data))
	i_acceleration = min((v.acceleration for v in data))
	i_prix = min((v.prix for v in data))
	i_pollution = min((v.pollution for v in data))

	return (i_puissance, i_couple, i_poids, i_acceleration, i_prix, i_pollution)

