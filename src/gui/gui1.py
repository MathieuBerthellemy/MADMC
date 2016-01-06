from Tkinter import *

class gui1:
	"""
		ATTRIBUTES:
			- voitures: Array<Voiture>
			- voiture: Voiture, la voiture a afficher
	"""
	def click_cb(self):
		if self.deal_with_puissance.get() == 0:
			self.selector.table.unset_column(0)
			self.selector.table.set_bounds(0, float("-inf"))
			self.maj()
			self.b_puissance.config(state=DISABLED)
			self.l_puissance.config(state=DISABLED)
			self.l_bound_puissance.config(state=DISABLED)
			self.radio_puissance.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(0)
			self.b_puissance.config(state=NORMAL)
			self.l_puissance.config(state=NORMAL)
			self.l_bound_puissance.config(state=NORMAL)
			self.radio_puissance.config(state=NORMAL)

		if self.deal_with_couple.get() == 0:
			self.selector.table.set_bounds(1, float("-inf"))
			self.maj()
			self.selector.table.unset_column(1)
			self.b_couple.config(state=DISABLED)
			self.l_couple.config(state=DISABLED)
			self.l_bound_couple.config(state=DISABLED)
			self.radio_couple.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(1)
			self.b_couple.config(state=NORMAL)
			self.l_couple.config(state=NORMAL)
			self.l_bound_couple.config(state=NORMAL)
			self.radio_couple.config(state=NORMAL)

		if self.deal_with_poids.get() == 0:
			self.selector.table.set_bounds(2, float("inf"))
			self.maj()
			self.selector.table.unset_column(2)
			self.b_poids.config(state=DISABLED)
			self.l_poids.config(state=DISABLED)
			self.l_bound_poids.config(state=DISABLED)
			self.radio_poids.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(2)
			self.b_poids.config(state=NORMAL)
			self.l_poids.config(state=NORMAL)
			self.l_bound_poids.config(state=NORMAL)
			self.radio_poids.config(state=NORMAL)

		if self.deal_with_acceleration.get() == 0:
			self.selector.table.set_bounds(3, float("inf"))
			self.maj()
			self.selector.table.unset_column(3)
			self.b_acceleration.config(state=DISABLED)
			self.l_acceleration.config(state=DISABLED)
			self.l_bound_acceleration.config(state=DISABLED)
			self.radio_acceleration.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(3)
			self.b_acceleration.config(state=NORMAL)
			self.l_acceleration.config(state=NORMAL)
			self.l_bound_acceleration.config(state=NORMAL)
			self.radio_acceleration.config(state=NORMAL)

		if self.deal_with_prix.get() == 0:
			self.selector.table.set_bounds(4, float("inf"))
			self.maj()
			self.selector.table.unset_column(4)
			self.b_prix.config(state=DISABLED)
			self.l_prix.config(state=DISABLED)
			self.l_bound_prix.config(state=DISABLED)
			self.radio_prix.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(4)
			self.b_prix.config(state=NORMAL)
			self.l_prix.config(state=NORMAL)
			self.l_bound_prix.config(state=NORMAL)
			self.radio_prix.config(state=NORMAL)

		if self.deal_with_pollution.get() == 0:
			self.selector.table.set_bounds(5, float("inf"))
			self.maj()
			self.selector.table.unset_column(5)
			self.b_pollution.config(state=DISABLED)
			self.l_pollution.config(state=DISABLED)
			self.l_bound_pollution.config(state=DISABLED)
			self.radio_pollution.config(state=DISABLED)
			
		else:
			self.selector.table.set_column(5)
			self.b_pollution.config(state=NORMAL)
			self.l_pollution.config(state=NORMAL)
			self.l_bound_pollution.config(state=NORMAL)
			self.radio_pollution.config(state=NORMAL)



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
		
		self.frame.config(text=self.voiture.nom)

		self.l_puissance.delete(0, END)
		self.l_couple.delete(0, END)
		self.l_poids.delete(0, END)
		self.l_acceleration.delete(0, END)
		self.l_prix.delete(0, END)
		self.l_pollution.delete(0, END)

		self.l_puissance.insert(0, self.voiture.puissance)
		self.l_couple.insert(0, self.voiture.couple)
		self.l_poids.insert(0, self.voiture.poids)
		self.l_acceleration.insert(0, self.voiture.get_float_acceleration())
		self.l_prix.insert(0, self.voiture.prix)
		self.l_pollution.insert(0, self.voiture.pollution)

		self.l_bound_puissance.delete(0, END)
		self.l_bound_couple.delete(0, END)
		self.l_bound_poids.delete(0, END)
		self.l_bound_acceleration.delete(0, END)
		self.l_bound_prix.delete(0, END)
		self.l_bound_pollution.delete(0, END)

		self.l_bound_puissance.insert(0, self.selector.table.bounds[0])
		self.l_bound_couple.insert(0, self.selector.table.bounds[1])
		self.l_bound_poids.insert(0, self.selector.table.bounds[2])
		self.l_bound_acceleration.insert(0, self.selector.table.bounds[3])
		self.l_bound_prix.insert(0, self.selector.table.bounds[4])
		self.l_bound_pollution.insert(0, self.selector.table.bounds[5])


	def _build_interface(self, w):
		self.l_image = Label(w)
		self.l_image.pack()


		#self.l_nom.grid(row=0, column=0, pady=10, padx=5)

		title = Label(w, text="MADMC", fg="lightgreen", font="Verdana 50 bold")
		title.pack(padx=20, pady=(0, 20))

		self.frame = LabelFrame(w, text="Description")
		self.frame.pack(expand=True, fill='both', padx=20, pady=(0, 20))

		
		offset = 1

		column_unit = 5
		column_bounds = 4
		column_opt = 3
		column_label = 2
		column_button = 1
		column_check_box = 0


		#CHECK BOX
		cb_puissance = Checkbutton(self.frame, variable=self.deal_with_puissance, command=self.click_cb)
		cb_puissance.grid(row=offset, column=column_check_box, pady=10, padx=0)
		cb_puissance.select()

		cb_couple = Checkbutton(self.frame, variable=self.deal_with_couple, command=self.click_cb)
		cb_couple.grid(row=offset+1, column=column_check_box, pady=10, padx=0)
		cb_couple.select()

		cb_poids = Checkbutton(self.frame, variable=self.deal_with_poids, command=self.click_cb)
		cb_poids.grid(row=offset+2, column=column_check_box, pady=10, padx=0)
		cb_poids.select()

		cb_acceleration = Checkbutton(self.frame, variable=self.deal_with_acceleration, command=self.click_cb)
		cb_acceleration.grid(row=offset+3, column=column_check_box, pady=10, padx=0)
		cb_acceleration.select()

		cb_prix = Checkbutton(self.frame, variable=self.deal_with_prix, command=self.click_cb)
		cb_prix.grid(row=offset+4, column=column_check_box, pady=10, padx=0)
		cb_prix.select()

		cb_pollution = Checkbutton(self.frame, variable=self.deal_with_pollution, command=self.click_cb)
		cb_pollution.grid(row=offset+5, column=column_check_box, pady=10, padx=0)
		cb_pollution.select()


		# BOUNDS
		self.l_bound_puissance = Entry(self.frame, width=7, foreground="red")
		self.l_bound_puissance.grid(row=offset, column=column_bounds, pady=10, padx=5)

		self.l_bound_couple = Entry(self.frame, width=7, foreground="red")
		self.l_bound_couple.grid(row=offset+1, column=column_bounds, pady=10, padx=5)

		self.l_bound_poids = Entry(self.frame, width=7, foreground="red")
		self.l_bound_poids.grid(row=offset+2, column=column_bounds, pady=10, padx=5)

		self.l_bound_acceleration = Entry(self.frame, width=7, foreground="red")
		self.l_bound_acceleration.grid(row=offset+3, column=column_bounds, pady=10, padx=5)

		self.l_bound_prix = Entry(self.frame, width=7, foreground="red")
		self.l_bound_prix.grid(row=offset+4, column=column_bounds, pady=10, padx=5)

		self.l_bound_pollution = Entry(self.frame, width=7, foreground="red")
		self.l_bound_pollution.grid(row=offset+5, column=column_bounds, pady=10, padx=5)

		

		#UNITE
		l_unite_puissance = Label(self.frame, text="ch")
		l_unite_puissance.grid(row=offset, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_couple = Label(self.frame, text="nm")
		l_unite_couple.grid(row=offset+1, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_poids = Label(self.frame, text="kg")
		l_unite_poids.grid(row=offset+2, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_acceleration = Label(self.frame, text="s")
		l_unite_acceleration.grid(row=offset+3, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_prix = Label(self.frame, text="e")
		l_unite_prix.grid(row=offset+4, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_pollution = Label(self.frame, text="g/km")
		l_unite_pollution.grid(row=offset+5, column=column_unit, pady=10, padx=2, sticky=W)


		#OPT
		l_opt_puissance = Label(self.frame, text=">")
		l_opt_puissance.grid(row=offset, column=column_opt, pady=10, padx=5)

		l_opt_couple = Label(self.frame, text=">")
		l_opt_couple.grid(row=offset+1, column=column_opt, pady=10, padx=5)

		l_opt_poids = Label(self.frame, text="<")
		l_opt_poids.grid(row=offset+2, column=column_opt, pady=10, padx=5)

		l_opt_acceleration = Label(self.frame, text="<")
		l_opt_acceleration.grid(row=offset+3, column=column_opt, pady=10, padx=5)

		l_opt_prix = Label(self.frame, text="<")
		l_opt_prix.grid(row=offset+4, column=column_opt, pady=10, padx=5)

		l_opt_pollution = Label(self.frame, text="<")
		l_opt_pollution.grid(row=offset+5, column=column_opt, pady=10, padx=5)

		# LABELS
		self.l_puissance = Entry(self.frame, width=7)
		self.l_puissance.grid(row=offset, column=column_label, pady=10, padx=5)

		self.l_couple = Entry(self.frame, width=7)
		self.l_couple.grid(row=offset+1, column=column_label, pady=10, padx=5)

		self.l_poids = Entry(self.frame, width=7)
		self.l_poids.grid(row=offset+2, column=column_label, pady=10, padx=5)

		self.l_acceleration = Entry(self.frame, width=7)
		self.l_acceleration.grid(row=offset+3, column=column_label, pady=10, padx=5)

		self.l_prix = Entry(self.frame, width=7)
		self.l_prix.grid(row=offset+4, column=column_label, pady=10, padx=5)

		self.l_pollution = Entry(self.frame, width=7)
		self.l_pollution.grid(row=offset+5, column=column_label, pady=10, padx=5)

		# BUTTONS
		b_puissance = Button(self.frame, text="Puissance",  command=lambda : self.click(0, self.voiture.puissance), width=10)
		b_puissance.grid(row=offset, column=0, pady=10, padx=5, sticky=W)

		b_couple = Button(self.frame, text="Couple",  command=lambda : self.click(1, self.voiture.couple), width=10)
		b_couple.grid(row=offset+1, column=0, pady=10, padx=5, sticky=W)

		b_poids = Button(self.frame, text="Poids",  command=lambda : self.click(2, self.voiture.poids), width=10)
		b_poids.grid(row=offset+2, column=0, pady=10, padx=5, sticky=W)

		b_acceleration = Button(self.frame, text="Acceleration",  command=lambda : self.click(3, self.voiture.get_float_acceleration()), width=10)
		b_acceleration.grid(row=offset+3, column=0, pady=10, padx=5, sticky=W)

		b_prix = Button(self.frame, text="Prix",  command=lambda : self.click(4, self.voiture.prix), width=10)
		b_prix.grid(row=offset+4, column=0, pady=10, padx=5, sticky=W)

		b_pollution = Button(self.frame, text="Pollution",  command=lambda : self.click(5, self.voiture.pollution), width=10)
		b_pollution.grid(row=offset+5, column=0, pady=10, padx=5, sticky=W)

		b_reset = Button(w, text="Reset",  command=lambda : self.click_reset(), width=10)
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

		self.deal_with_puissance = IntVar()
		self.deal_with_couple = IntVar()
		self.deal_with_poids = IntVar()
		self.deal_with_acceleration = IntVar()
		self.deal_with_prix = IntVar()
		self.deal_with_pollution = IntVar()

		self._build_interface(w)   

		self.maj()
		w.mainloop()