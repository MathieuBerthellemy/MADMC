from Selectors import *
from Data import *
from file_loader import *

def lauch():
	#path = filedialog.askopenfilename(filetypes=[("Textfiles","*.csv")])
	path = "data.csv"
	if path:
		voitures = load_file(path)
		selector = Selector_Tchebycheff(voitures)

		ok = False
		while not ok:
			if not selector.data_is_empty():
				best = selector.get_balanced_solution()
				print("Meilleur compromis: ")
				best.to_string()

				ok = (int(input("satisfait ? (0/1)")) == 1)

				if not ok:
					c = int(input("critère à améliorer"))

					if c == 1:
						selector.cut(voitures, c, best.puissance, "max")
					elif c == 2:
						selector.cut(voitures, c, best.couple, "max")
					elif c == 3:
						selector.cut(voitures, c, best.poids, "min")
					elif c == 4:
						selector.cut(voitures, c, best.get_float_acceleration(), "min")
					elif c == 5:
						selector.cut(voitures, c, best.prix, "min")
					elif c == 6:
						selector.cut(voitures, c, best.pollution, "min")
			else:
				print("plus de solution trouvée")
				break

	else:
		print("fail")



lauch()