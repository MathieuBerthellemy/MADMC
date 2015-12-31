from Tkinter import *
import random as rd

class gui2:
	"""
		ATTRIBUTES:
			voitures: Array<Voiture>
			selector: le selector utiliser pour generer des solutions
			voiture1: Voiture, la voiture a afficher a gauche
			voiture2: Voiture, la voiture a afficehr a droite
	"""
	def click_reset(self):
		"""
			Le decideur annonce vouloir recomencer la selection
		"""
		self.selector.reset_preferences()
		self.voiture1 = rd.choice(self.voitures)
		self.voiture2 = rd.choice(self.voitures)
		self.maj()

	def click_v1_pref_v2(self):
		"""
			Le decideur annonce preferer voiture1 a voiture2
		"""
		self.selector.add_preference((self.voiture1.vectorize(), self.voiture2.vectorize()))
		new_alt = self.selector.get_solution()
		self.voiture2 = self.voitures[new_alt]
		self.maj()

	def click_v2_pref_v1(self):
		"""
			Le decideur annonce preferer voiture2 a voiture1
		"""
		self.selector.add_preference((self.voiture2.vectorize(), self.voiture1.vectorize()))
		new_alt = self.selector.get_solution()
		self.voiture1 = self.voitures[new_alt]
		self.maj()


	def _build_interface(self, w):
		master = Frame(w)
		master.pack()

		self.frame1 = LabelFrame(master, text="Description")
		self.frame1.pack(expand=True, fill='both', padx=20, pady=(10, 20), side=LEFT)


		frame_button = Frame(master)
		b_v1_v2 = Button(frame_button, text=">",  command=self.click_v1_pref_v2)
		b_v1_v2.pack()

		b_v2_v1 = Button(frame_button, text="<",  command=self.click_v2_pref_v1)
		b_v2_v1.pack()

		b_reset = Button(frame_button, text="reset",  command=self.click_reset)
		b_reset.pack()
		frame_button.pack(side=LEFT)


		self.frame2 = LabelFrame(master, text="Description")
		self.frame2.pack(expand=True, fill='both', padx=20, pady=(10, 20), side=LEFT)

		offset = 1

		# LABELS
		self.l_puissance1 = Entry(self.frame1)
		self.l_puissance1.grid(row=offset, column=1, pady=10, padx=5)

		self.l_couple1 = Entry(self.frame1)
		self.l_couple1.grid(row=offset+1, column=1, pady=10, padx=5)

		self.l_poids1 = Entry(self.frame1)
		self.l_poids1.grid(row=offset+2, column=1, pady=10, padx=5)

		self.l_acceleration1 = Entry(self.frame1)
		self.l_acceleration1.grid(row=offset+3, column=1, pady=10, padx=5)

		self.l_prix1 = Entry(self.frame1)
		self.l_prix1.grid(row=offset+4, column=1, pady=10, padx=5)

		self.l_pollution1 = Entry(self.frame1)
		self.l_pollution1.grid(row=offset+5, column=1, pady=10, padx=5)

		# LABELS
		b_puissance1 = Label(self.frame1, text="Puissance")
		b_puissance1.grid(row=offset, column=0, pady=10, padx=5, sticky=W)

		b_couple1 = Label(self.frame1, text="Couple")
		b_couple1.grid(row=offset+1, column=0, pady=10, padx=5, sticky=W)

		b_poids1 = Label(self.frame1, text="Poids")
		b_poids1.grid(row=offset+2, column=0, pady=10, padx=5, sticky=W)

		b_acceleration1 = Label(self.frame1, text="Acceleration")
		b_acceleration1.grid(row=offset+3, column=0, pady=10, padx=5, sticky=W)

		b_prix1 = Label(self.frame1, text="Prix")
		b_prix1.grid(row=offset+4, column=0, pady=10, padx=5, sticky=W)

		b_pollution1 = Label(self.frame1, text="Pollution")
		b_pollution1.grid(row=offset+5, column=0, pady=10, padx=5, sticky=W)


		# LABELS
		self.l_puissance2 = Entry(self.frame2)
		self.l_puissance2.grid(row=offset, column=1, pady=10, padx=5)

		self.l_couple2 = Entry(self.frame2)
		self.l_couple2.grid(row=offset+1, column=1, pady=10, padx=5)

		self.l_poids2 = Entry(self.frame2)
		self.l_poids2.grid(row=offset+2, column=1, pady=10, padx=5)

		self.l_acceleration2 = Entry(self.frame2)
		self.l_acceleration2.grid(row=offset+3, column=1, pady=10, padx=5)

		self.l_prix2 = Entry(self.frame2)
		self.l_prix2.grid(row=offset+4, column=1, pady=10, padx=5)

		self.l_pollution2 = Entry(self.frame2)
		self.l_pollution2.grid(row=offset+5, column=1, pady=10, padx=5)

		# LABELS
		b_puissance2 = Label(self.frame2, text="Puissance")
		b_puissance2.grid(row=offset, column=0, pady=10, padx=5, sticky=W)

		b_couple2 = Label(self.frame2, text="Couple")
		b_couple2.grid(row=offset+1, column=0, pady=10, padx=5, sticky=W)

		b_poids2 = Label(self.frame2, text="Poids")
		b_poids2.grid(row=offset+2, column=0, pady=10, padx=5, sticky=W)

		b_acceleration2 = Label(self.frame2, text="Acceleration")
		b_acceleration2.grid(row=offset+3, column=0, pady=10, padx=5, sticky=W)

		b_prix2 = Label(self.frame2, text="Prix")
		b_prix2.grid(row=offset+4, column=0, pady=10, padx=5, sticky=W)

		b_pollution2 = Label(self.frame2, text="Pollution")
		b_pollution2.grid(row=offset+5, column=0, pady=10, padx=5, sticky=W)



	def maj(self):
		"""
			Met a jour l'interface graphique, les attributs de voiture1 et voiture2 sont mis dans les labels prevus a cet effet
		"""
		self.frame1.config(text=self.voiture1.nom)

		self.l_puissance1.delete(0, END)
		self.l_couple1.delete(0, END)
		self.l_poids1.delete(0, END)
		self.l_acceleration1.delete(0, END)
		self.l_prix1.delete(0, END)
		self.l_pollution1.delete(0, END)

		self.l_puissance1.insert(0, self.voiture1.format_puissance())
		self.l_couple1.insert(0, self.voiture1.format_couple())
		self.l_poids1.insert(0, self.voiture1.format_poids())
		self.l_acceleration1.insert(0, self.voiture1.format_acceleration())
		self.l_prix1.insert(0, self.voiture1.format_prix())
		self.l_pollution1.insert(0, self.voiture1.format_pollution())

		self.frame2.config(text=self.voiture2.nom)

		self.l_puissance2.delete(0, END)
		self.l_couple2.delete(0, END)
		self.l_poids2.delete(0, END)
		self.l_acceleration2.delete(0, END)
		self.l_prix2.delete(0, END)
		self.l_pollution2.delete(0, END)

		self.l_puissance2.insert(0, self.voiture2.format_puissance())
		self.l_couple2.insert(0, self.voiture2.format_couple())
		self.l_poids2.insert(0, self.voiture2.format_poids())
		self.l_acceleration2.insert(0, self.voiture2.format_acceleration())
		self.l_prix2.insert(0, self.voiture2.format_prix())
		self.l_pollution2.insert(0, self.voiture2.format_pollution())



	def __init__(self, voitures, selector):
		w = Tk()
		w.resizable(0,0)
		w.title("MADMC - Car selector")

		self.voitures = voitures
		self.selector = selector

		self._build_interface(w)   

		self.click_reset()
		
		self.maj()
		w.mainloop()