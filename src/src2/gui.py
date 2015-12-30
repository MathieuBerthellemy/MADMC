from Tkinter import *
import random as rd

class gui:

	def click_v1_pref_v2(self):
		self.selector.add_pref(voiture1, voiture2)

		new_alt = self.selector.get()
		voiture2 = new_alt

	def click_v2_pref_v1(self):
		self.selector.add_pref(voiture2, voiture1)

		new_alt = self.selector.get()
		voiture1 = new_alt


	def _build_interface(self, w):
		master = Frame(w)
		master.pack()

		self.frame1 = LabelFrame(master, text="Description")
		self.frame1.pack(expand=True, fill='both', padx=20, pady=(10, 20), side=LEFT)


		frame_button = Frame(master)
		b_reset = Button(frame_button, text=">",  command=self.click_v1_pref_v2)
		b_reset.pack()

		b_reset = Button(frame_button, text="<",  command=self.click_v2_pref_v1)
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

		self.voiture1 = rd.choice(voitures)
		self.voiture2 = rd.choice(voitures)
		
		self.maj()
		w.mainloop()