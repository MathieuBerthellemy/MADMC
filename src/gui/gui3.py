
from Tkinter import *
from Data import *


class gui3:
	"""
		ATTRIBUTES:
			voitures
			selector
			knapsack
			voitureSum
	"""

	def solve(self):
		solution = self.selector.get_solution()
		self.knapsack = []
		for i in solution:
			self.knapsack.append(self.voitures[i])
		
	def click(self, column, bound):
		self.selector.cut(column, bound)
		self.solve()
		self.maj()

	def click_reset(self):
		self.selector.reset_bounds()
		self.solve()
		self.maj()

	def __init__(self, voitures, selector):
		w = Tk()
		w.resizable(0,0)
		w.title("MADMC - Knapsack")

		self.voitures = voitures
		self.selector = selector

		self.solve()

		self._build_interface(w)   

		self.maj()
		w.mainloop()

	def sum_acceleration(self):
		output_a = 0
		output_b = 0
		for v in self.voitures:
			output_a += v.acceleration[0]
			output_b += v.acceleration[1]
		return (output_a, output_b)

	def maj(self):
		"""
			Met a jour l'interface graphique, les attributs de voiture sont mis dans les labels prevus a cet effet
		"""
		
		puissance_cum = sum([v.puissance for v in self.knapsack])
		couple_cum = sum([v.couple for v in self.knapsack])
		poids_cum = sum([v.poids for v in self.knapsack])
		acceleration_cum = self.sum_acceleration()
		prix_cum = sum([v.prix for v in self.knapsack])
		pollution_cum = sum([v.pollution for v in self.knapsack])

		self.voitureSum = Voiture("sum", puissance_cum, couple_cum, poids_cum, '0"0', prix_cum, pollution_cum)
		self.voitureSum.acceleration = acceleration_cum

		self.l_puissance.delete(0, END)
		self.l_couple.delete(0, END)
		self.l_poids.delete(0, END)
		self.l_acceleration.delete(0, END)
		self.l_prix.delete(0, END)
		self.l_pollution.delete(0, END)

		self.l_puissance.insert(0, self.voitureSum.format_puissance())
		self.l_couple.insert(0, self.voitureSum.format_couple())
		self.l_poids.insert(0, self.voitureSum.format_poids())
		self.l_acceleration.insert(0, self.voitureSum.format_acceleration())
		self.l_prix.insert(0, self.voitureSum.format_prix())
		self.l_pollution.insert(0, self.voitureSum.format_pollution())
		
		self.listbox.delete(0, END)
		for v in self.knapsack:
			self.listbox.insert(END, v.nom)


	def _build_interface(self, w):

		frame = LabelFrame(w, text="Description")
		frame.pack(expand=True, fill='both', padx=30, pady=30, side=LEFT)

		offset = 1

		# LABELS
		self.l_puissance = Entry(frame)
		self.l_puissance.grid(row=offset, column=1, pady=10, padx=5)

		self.l_couple = Entry(frame)
		self.l_couple.grid(row=offset+1, column=1, pady=10, padx=5)

		self.l_poids = Entry(frame)
		self.l_poids.grid(row=offset+2, column=1, pady=10, padx=5)

		self.l_acceleration = Entry(frame)
		self.l_acceleration.grid(row=offset+3, column=1, pady=10, padx=5)

		self.l_prix = Entry(frame)
		self.l_prix.grid(row=offset+4, column=1, pady=10, padx=5)

		self.l_pollution = Entry(frame)
		self.l_pollution.grid(row=offset+5, column=1, pady=10, padx=5)

		# BUTTONS
		b_puissance = Button(frame, text="Puissance",  command=lambda : self.click(0, self.voitureSum.puissance))
		b_puissance.grid(row=offset, column=0, pady=10, padx=5, sticky=W)

		b_couple = Button(frame, text="Couple",  command=lambda : self.click(1, self.voitureSum.couple))
		b_couple.grid(row=offset+1, column=0, pady=10, padx=5, sticky=W)

		b_poids = Button(frame, text="Poids",  command=lambda : self.click(2, self.voitureSum.poids))
		b_poids.grid(row=offset+2, column=0, pady=10, padx=5, sticky=W)

		b_acceleration = Button(frame, text="Acceleration",  command=lambda : self.click(3, self.voitureSum.get_float_acceleration()))
		b_acceleration.grid(row=offset+3, column=0, pady=10, padx=5, sticky=W)

		b_prix = Button(frame, text="Prix",  command=lambda : self.click(4, self.voitureSum.prix))
		b_prix.grid(row=offset+4, column=0, pady=10, padx=5, sticky=W)

		b_pollution = Button(frame, text="Pollution",  command=lambda : self.click(5, self.voitureSum.pollution))
		b_pollution.grid(row=offset+5, column=0, pady=10, padx=5, sticky=W)

		b_reset = Button(frame, text="Reset",  command=lambda : self.click_reset())
		b_reset.grid(row=offset+6, column=1, pady=10, padx=5, sticky=W)
	
		self.listbox = Listbox(w)
		self.listbox.pack(expand=True, fill='both', padx=(0, 30), pady=(30, 30), side=LEFT)
			
		
