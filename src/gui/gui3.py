
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

		try:
			solution = self.selector.get_solution(self.column_weight.get())
			self.knapsack = []
			for i in solution:
				self.knapsack.append(self.voitures[i])
		except GurobiError:
			print "ERROR"

		
		
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

		self.deal_with_puissance = IntVar()
		self.deal_with_couple = IntVar()
		self.deal_with_poids = IntVar()
		self.deal_with_acceleration = IntVar()
		self.deal_with_prix = IntVar()
		self.deal_with_pollution = IntVar()

		self.column_weight = IntVar()

		self._build_interface(w)   
		self.solve()

		self.maj()
		w.mainloop()

	def sum_acceleration(self):
		output_a = 0
		output_b = 0
		for v in self.knapsack:
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

		print self.voitureSum.vectorize()

		self.l_puissance.delete(0, END)
		self.l_couple.delete(0, END)
		self.l_poids.delete(0, END)
		self.l_acceleration.delete(0, END)
		self.l_prix.delete(0, END)
		self.l_pollution.delete(0, END)

		self.l_puissance.insert(0, self.voitureSum.puissance)
		self.l_couple.insert(0, self.voitureSum.couple)
		self.l_poids.insert(0, self.voitureSum.poids)
		self.l_acceleration.insert(0, self.voitureSum.get_float_acceleration())
		self.l_prix.insert(0, self.voitureSum.prix)
		self.l_pollution.insert(0, self.voitureSum.pollution)

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
		
		self.listbox.delete(0, END)
		for v in self.knapsack:
			self.listbox.insert(END, v.nom)


	def _build_interface(self, w):

		title = Label(w, text="MADMC", fg="lightgreen", font="Verdana 50 bold")
		title.pack(padx=20, pady=(20, 0))

		frame = LabelFrame(w, text="KnapSack description")
		frame.pack(expand=True, fill='both', padx=30, pady=20, side=LEFT)

		offset = 1

		column_radio = 6
		column_unit = 5
		column_bounds = 4
		column_opt = 3
		column_label = 2
		column_button = 1
		column_check_box = 0

		#CHECK BOX
		cb_puissance = Checkbutton(frame, variable=self.deal_with_puissance, command=self.click_cb)
		cb_puissance.grid(row=offset, column=column_check_box, pady=10, padx=0)
		cb_puissance.select()

		cb_couple = Checkbutton(frame, variable=self.deal_with_couple, command=self.click_cb)
		cb_couple.grid(row=offset+1, column=column_check_box, pady=10, padx=0)
		cb_couple.select()

		cb_poids = Checkbutton(frame, variable=self.deal_with_poids, command=self.click_cb)
		cb_poids.grid(row=offset+2, column=column_check_box, pady=10, padx=0)
		cb_poids.select()

		cb_acceleration = Checkbutton(frame, variable=self.deal_with_acceleration, command=self.click_cb)
		cb_acceleration.grid(row=offset+3, column=column_check_box, pady=10, padx=0)
		cb_acceleration.select()

		cb_prix = Checkbutton(frame, variable=self.deal_with_prix, command=self.click_cb)
		cb_prix.grid(row=offset+4, column=column_check_box, pady=10, padx=0)
		cb_prix.select()

		cb_pollution = Checkbutton(frame, variable=self.deal_with_pollution, command=self.click_cb)
		cb_pollution.grid(row=offset+5, column=column_check_box, pady=10, padx=0)
		cb_pollution.select()

		# BOUNDS
		self.l_bound_puissance = Entry(frame, width=7, foreground="red")
		self.l_bound_puissance.grid(row=offset, column=column_bounds, pady=10, padx=5)

		self.l_bound_couple = Entry(frame, width=7, foreground="red")
		self.l_bound_couple.grid(row=offset+1, column=column_bounds, pady=10, padx=5)

		self.l_bound_poids = Entry(frame, width=7, foreground="red")
		self.l_bound_poids.grid(row=offset+2, column=column_bounds, pady=10, padx=5)

		self.l_bound_acceleration = Entry(frame, width=7, foreground="red")
		self.l_bound_acceleration.grid(row=offset+3, column=column_bounds, pady=10, padx=5)

		self.l_bound_prix = Entry(frame, width=7, foreground="red")
		self.l_bound_prix.grid(row=offset+4, column=column_bounds, pady=10, padx=5)

		self.l_bound_pollution = Entry(frame, width=7, foreground="red")
		self.l_bound_pollution.grid(row=offset+5, column=column_bounds, pady=10, padx=5)


		#OPT
		l_opt_puissance = Label(frame, text=">")
		l_opt_puissance.grid(row=offset, column=column_opt, pady=10, padx=5)

		l_opt_couple = Label(frame, text=">")
		l_opt_couple.grid(row=offset+1, column=column_opt, pady=10, padx=5)

		l_opt_poids = Label(frame, text="<")
		l_opt_poids.grid(row=offset+2, column=column_opt, pady=10, padx=5)

		l_opt_acceleration = Label(frame, text="<")
		l_opt_acceleration.grid(row=offset+3, column=column_opt, pady=10, padx=5)

		l_opt_prix = Label(frame, text="<")
		l_opt_prix.grid(row=offset+4, column=column_opt, pady=10, padx=5)

		l_opt_pollution = Label(frame, text="<")
		l_opt_pollution.grid(row=offset+5, column=column_opt, pady=10, padx=5)

		#UNITE
		l_unite_puissance = Label(frame, text="ch")
		l_unite_puissance.grid(row=offset, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_couple = Label(frame, text="nm")
		l_unite_couple.grid(row=offset+1, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_poids = Label(frame, text="kg")
		l_unite_poids.grid(row=offset+2, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_acceleration = Label(frame, text="s")
		l_unite_acceleration.grid(row=offset+3, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_prix = Label(frame, text="e")
		l_unite_prix.grid(row=offset+4, column=column_unit, pady=10, padx=2, sticky=W)

		l_unite_pollution = Label(frame, text="g/km")
		l_unite_pollution.grid(row=offset+5, column=column_unit, pady=10, padx=2, sticky=W)



		# LABELS
		self.l_puissance = Entry(frame, width=7)
		self.l_puissance.grid(row=offset, column=column_label, pady=10, padx=5)

		self.l_couple = Entry(frame, width=7)
		self.l_couple.grid(row=offset+1, column=column_label, pady=10, padx=5)

		self.l_poids = Entry(frame, width=7)
		self.l_poids.grid(row=offset+2, column=column_label, pady=10, padx=5)

		self.l_acceleration = Entry(frame, width=7)
		self.l_acceleration.grid(row=offset+3, column=column_label, pady=10, padx=5)

		self.l_prix = Entry(frame, width=7)
		self.l_prix.grid(row=offset+4, column=column_label, pady=10, padx=5)

		self.l_pollution = Entry(frame, width=7)
		self.l_pollution.grid(row=offset+5, column=column_label, pady=10, padx=5)

		# BUTTONS
		self.b_puissance = Button(frame, text="Puissance",  command=lambda : self.click(0, self.voitureSum.puissance), width=10)
		self.b_puissance.grid(row=offset, column=column_button, pady=10, padx=5, sticky=W)

		self.b_couple = Button(frame, text="Couple",  command=lambda : self.click(1, self.voitureSum.couple), width=10)
		self.b_couple.grid(row=offset+1, column=column_button, pady=10, padx=5, sticky=W)

		self.b_poids = Button(frame, text="Poids",  command=lambda : self.click(2, self.voitureSum.poids), width=10)
		self.b_poids.grid(row=offset+2, column=column_button, pady=10, padx=5, sticky=W)

		self.b_acceleration = Button(frame, text="Acceleration",  command=lambda : self.click(3, self.voitureSum.get_float_acceleration()), width=10)
		self.b_acceleration.grid(row=offset+3, column=column_button, pady=10, padx=5, sticky=W)

		self.b_prix = Button(frame, text="Prix",  command=lambda : self.click(4, self.voitureSum.prix), width=10)
		self.b_prix.grid(row=offset+4, column=column_button, pady=10, padx=5, sticky=W)

		self.b_pollution = Button(frame, text="Pollution",  command=lambda : self.click(5, self.voitureSum.pollution), width=10)
		self.b_pollution.grid(row=offset+5, column=column_button, pady=10, padx=5, sticky=W)

		b_reset = Button(frame, text="Reset",  command=lambda : self.click_reset())
		b_reset.grid(row=offset+6, column=2, pady=10, padx=5, sticky=E)
	
		self.listbox = Listbox(w)
		self.listbox.pack(expand=True, fill='both', padx=(0, 30), pady=(30, 30), side=LEFT)
			
		# RADIO BUTTON
		self.radio_puissance = Radiobutton(frame, variable=self.column_weight, val=0)
		self.radio_puissance.grid(row=offset, column=column_radio, pady=10, padx=5, sticky=W)

		self.radio_couple = Radiobutton(frame, variable=self.column_weight, val=1)
		self.radio_couple.grid(row=offset+1, column=column_radio, pady=10, padx=5, sticky=W)

		self.radio_poids = Radiobutton(frame, variable=self.column_weight, val=2)
		self.radio_poids.grid(row=offset+2, column=column_radio, pady=10, padx=5, sticky=W)
	
		self.radio_acceleration = Radiobutton(frame, variable=self.column_weight, val=3)
		self.radio_acceleration.grid(row=offset+3, column=column_radio, pady=10, padx=5, sticky=W)
	
		self.radio_prix = Radiobutton(frame, variable=self.column_weight, val=4)
		self.radio_prix.grid(row=offset+4, column=column_radio, pady=10, padx=5, sticky=W)
	
		self.radio_pollution = Radiobutton(frame, variable=self.column_weight, val=5)
		self.radio_pollution.grid(row=offset+5, column=column_radio, pady=10, padx=5, sticky=W)
		self.radio_prix.invoke()
		
