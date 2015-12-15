import csv
import tkinter as tk
from tkinter import filedialog, Tk, Label
from Data import *

def load_file(path):
	output = []

	with open(path, 'r') as csvfile:
		cr = csv.reader(csvfile, delimiter=';')

		for row in cr:
			output.append(Voiture(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	return output
