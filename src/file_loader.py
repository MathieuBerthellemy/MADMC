import csv
import tkinter as tk
from tkinter import filedialog, Tk, Label
from Voiture import *
from tools_box import *


def load_file(path):
	output = []

	with open(path, 'r') as csvfile:
		cr = csv.reader(csvfile, delimiter=';')

		for row in cr:
			output.append(Voiture(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	return output



def lauch():
	#path = filedialog.askopenfilename(filetypes=[("Textfiles","*.csv")])
	path = "data.csv"
	if path:
		voitures = load_file(path)


		for v in voitures:
			print(v.nom, v.format_puissance(), v.format_couple(), v.format_poids(), v.format_acceleration(), v.format_prix(), v.format_pollution())


		print(get_nadir(voitures))
		print(get_ideal(voitures))
	else:
		print("fail")

lauch()