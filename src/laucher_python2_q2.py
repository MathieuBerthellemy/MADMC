from src2 import *
from Data import *
from file_loader import *


path = "data.csv"
if path:
	voitures = load_file(path)
	gui(voitures, None)

