from tkinter import *
import time
import random

class Animacion():

	def __init__(self):
		self.ventana = Tk()
		self.canvas = Canvas(self.ventana,width=400,height=400)
		self.ventana.geometry("400x400")
		self.canvas.place(x=0,y=0)
		self.fondo = self.canvas.create_rectangle(0,0,400,400,fill='black')
		self.tronco = self.canvas.create_rectangle(170,210,230,310,fill='brown')
		self.estrella = self.canvas.create_oval(180,20,220,50,fill='yellow')
		self.arbol = self.canvas.create_polygon(60,210,340,210,200,50,fill='green')
		self.lista = []
		self.contador = 0
		self.crear()
		self.ventana.after(300,self.animacion)
		self.ventana.mainloop()

	def crear(self):
		r = random.randint(-400,400)
		self.copo = self.canvas.create_oval(r,10,r+3,13,fill='white')
		self.contador+=1
		self.lista.append(self.copo)
		if self.contador<100:
			self.ventana.after(40,self.crear)

	def animacion(self):
		while True:
			for copo in self.lista:
				coor = self.canvas.coords(copo)
				x = 1
				y = 1
				if coor[0]>=400:
					x=-400
				if coor[1]>=400:
					y=-400
				self.canvas.move(copo,x,y)
			self.canvas.update()
			
obj = Animacion()