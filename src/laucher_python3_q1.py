from src1 import *
from Data import *
from file_loader import *

def fill_table(voitures, table):
	i = 0
	for voiture in voitures:
		table.add_row(i, voiture.vectorize())
		i += 1


def lauch1(voitures):
	selector = SelectorTchebycheff(table)
	gui(voitures, selector)

def lauch2(voitures):
	#path = filedialog.askopenfilename(filetypes=[("Textfiles","*.csv")])
	interactor = Interactor_human()
	selector = SelectorTchebycheff(table)
	ok = False
	while not ok:
		idbest = selector.get_balanced_solution()
		if idbest != None:
			best = voitures[idbest]
			print("Meilleur compromis: ")
			best.to_string()

			ok = interactor.get_satisfait()

			if not ok:
				c = interactor.get_critere()

				if c == 1:
					bound = best.puissance
				elif c == 2:
					bound = best.couple
				elif c == 3:
					bound = best.poids
				elif c == 4:
					bound = best.get_float_acceleration()
				elif c == 5:
					bound = best.prix
				elif c == 6:
					bound = best.pollution

				selector.cut(c-1, bound)
		else:
			print("plus de solution trouvee")
			break

	else:
		print("fail")


path = "data.csv"
if path:
	voitures = load_file(path)
	table = AlternativesTable(("puissance", Opt.MAX), ("couple", Opt.MAX), ("poids", Opt.MIN), ("acceleration", Opt.MIN), ("prix", Opt.MIN), ("pollution", Opt.MIN))
	fill_table(voitures, table);

	lauch1(voitures)

