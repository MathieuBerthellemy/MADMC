from Tkinter import *

class gui1:
	"""
		ATTRIBUTES:
			- voitures: Array<Voiture>
			- voiture: Voiture, la voiture a afficher
	"""
	def solve(self):
		id_best = self.selector.get_balanced_solution()
		
		if id_best != None:
			self.voiture = self.voitures[id_best]

			self.maj()

	def click_reset(self):
		self.selector.reset_bounds()
		self.solve()

	def click(self, critere, bound):

		self.selector.cut(critere, bound)

		self.solve()

	def maj(self):
		"""
			Met a jour l'interface graphique, les attributs de voiture sont mis dans les labels prevus a cet effet
		"""
		
		self.l_nom.config(text=self.voiture.nom)

		self.l_puissance.delete(0, END)
		self.l_couple.delete(0, END)
		self.l_poids.delete(0, END)
		self.l_acceleration.delete(0, END)
		self.l_prix.delete(0, END)
		self.l_pollution.delete(0, END)

		self.l_puissance.insert(0, self.voiture.format_puissance())
		self.l_couple.insert(0, self.voiture.format_couple())
		self.l_poids.insert(0, self.voiture.format_poids())
		self.l_acceleration.insert(0, self.voiture.format_acceleration())
		self.l_prix.insert(0, self.voiture.format_prix())
		self.l_pollution.insert(0, self.voiture.format_pollution())


	def _build_interface(self, w):
		self.l_image = Label(w)
		self.l_image.pack()

		self.l_nom = Label(w)
		self.l_nom.pack()
		#self.l_nom.grid(row=0, column=0, pady=10, padx=5)

		frame = LabelFrame(w, text="Description")
		frame.pack(expand=True, fill='both', padx=20, pady=(0, 20))

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
		b_puissance = Button(frame, text="Puissance",  command=lambda : self.click(0, self.voiture.puissance))
		b_puissance.grid(row=offset, column=0, pady=10, padx=5, sticky=W)

		b_couple = Button(frame, text="Couple",  command=lambda : self.click(1, self.voiture.couple))
		b_couple.grid(row=offset+1, column=0, pady=10, padx=5, sticky=W)

		b_poids = Button(frame, text="Poids",  command=lambda : self.click(2, self.voiture.poids))
		b_poids.grid(row=offset+2, column=0, pady=10, padx=5, sticky=W)

		b_acceleration = Button(frame, text="Acceleration",  command=lambda : self.click(3, self.voiture.get_float_acceleration()))
		b_acceleration.grid(row=offset+3, column=0, pady=10, padx=5, sticky=W)

		b_prix = Button(frame, text="Prix",  command=lambda : self.click(4, self.voiture.prix))
		b_prix.grid(row=offset+4, column=0, pady=10, padx=5, sticky=W)

		b_pollution = Button(frame, text="Pollution",  command=lambda : self.click(5, self.voiture.pollution))
		b_pollution.grid(row=offset+5, column=0, pady=10, padx=5, sticky=W)

		b_reset = Button(w, text="Reset",  command=lambda : self.click_reset())
		b_reset.grid(row=offset+5, column=0, pady=5, padx=5, sticky=N)
		b_reset.pack()

	def __init__(self, voitures, selector):
		w = Tk()
		w.resizable(0,0)
		w.title("MADMC - Tchebycheff")

		self.voitures = voitures
		self.selector = selector

		id_best = self.selector.get_balanced_solution()
		self.voiture = voitures[id_best]

		self._build_interface(w)   

		self.maj()
		w.mainloop()