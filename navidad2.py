from tkinter import *
import time
import random

class Animacion():
	def __init__(self):
		self.ventana = Tk()
		self.canvas = Canvas(self.ventana,width=400,height=400)
		self.ventana.geometry("400x400")
		self.canvas.place(x=0,y=0)
		self.canvas.create_rectangle(0,0,400,400,fill='black')
		self.canvas.create_oval(180,20,220,50,fill='yellow')
		self.canvas.create_polygon(60,110,340,110,200,50,fill='green')
		self.canvas.create_polygon(60,160,340,160,200,90,fill='green')
		self.canvas.create_polygon(60,210,340,210,200,130,fill='green')
		self.canvas.create_oval(320,110,350,125,fill='blue')
		self.canvas.create_oval(60,110,90,125,fill='red')
		self.canvas.create_oval(320,160,350,175,fill='green')
		self.canvas.create_oval(60,160,90,175,fill='brown')
		self.canvas.create_oval(320,210,350,225,fill='yellow')
		self.canvas.create_oval(60,210,90,225,fill='gray')
		self.canvas.create_rectangle(170,210,230,310,fill='brown')
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
			self.ventana.after(30,self.crear)
		
	def animacion(self):
		while True:
			for copo in self.lista:
				coordenadas=self.canvas.coords(copo)
				x=1
				y=1
				if coordenadas[0]>=400:
					x=-400
				if coordenadas[1]>=400:
					y=-400
				self.canvas.move(copo,x,y)
			self.canvas.update()

obj = Animacion()