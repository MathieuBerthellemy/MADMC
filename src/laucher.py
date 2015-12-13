from tools_box import *
from Voiture import *
from file_loader import *

def lauch():
	#path = filedialog.askopenfilename(filetypes=[("Textfiles","*.csv")])
	path = "data.csv"
	if path:
		voitures = load_file(path)

		ok = False
		while not ok:
			if len(voitures) > 0:
				best = get_balanced_solution(voitures)
				print("Meilleur compromis: ")
				best.to_string()

				ok = (int(input("satisfait ? (0/1)")) == 1)

				if not ok:
					c = int(input("critère à améliorer"))

					if c == 1:
						voitures = cut(voitures, c, best.puissance, "max")
					elif c == 2:
						voitures = cut(voitures, c, best.couple, "max")
					elif c == 3:
						voitures = cut(voitures, c, best.poids, "min")
					elif c == 4:
						voitures = cut(voitures, c, best.get_float_acceleration(), "min")
					elif c == 5:
						voitures = cut(voitures, c, best.prix, "min")
					elif c == 6:
						voitures = cut(voitures, c, best.pollution, "min")
			else:
				print("plus de solution trouvée")
				break

	else:
		print("fail")

def cut(data, critere, value, orientation):
	output = []
	for v in data:
		vector = v.vectorize()
		if (orientation == "max" and vector[critere-1] > value) or (orientation == "min" and vector[critere-1] < value):
			output.append(v)
	return output

lauch()