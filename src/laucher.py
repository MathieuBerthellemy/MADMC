from gui import *
from Data import *
from file_loader import *
from Selector_library import *


def fill_table(voitures, table):
	"""
		Remplis la table donnee en parametre avec les donness (ici des voitures) donnees en parametre
	"""
	i = 0
	for voiture in voitures:
		table.add_row(i, voiture.vectorize())
		i += 1

def lauch1(voitures, table):
	"""
		Partie 1
	"""
	selector = SelectorTchebycheff(table)
	gui1(voitures, selector)

def lauch2(voitures, table):
	"""
		Partie 2
	"""
	selector = SelectorMinMaxRegret(table)
	gui2(voitures, selector)


def lauch3(voitures, table):
	"""
		Partie 3
	"""
	selector = SelectorKnapSack(table)
	gui3(voitures, selector)
	



path = "data.csv"
if path:
	voitures = load_file(path)
	table = AlternativesTable("puissance", "couple", "poids", "acceleration", "prix", "pollution")
	table.set_col_max(0, 1)
	table.set_col_min(2, 3, 4, 5)
	fill_table(voitures, table);

	lauch1(voitures, table)
	lauch2(voitures, table)
	lauch3(voitures, table)
