#########
#Gesturas de posición
#GRID

#Grid: Crea una malla en toda la ventana para acceder 
#a manera de matriz mediante columnas y filas

from tkinter import *
#Creamos nuestra ventana
v=Tk()

i=0
"""
for x in range(6):
	for y in range(6):
		i+=1
		Button(v,text=str(i),borderwidth=1,width=10,height=10).grid(row=x,column=y)
"""

botonIzq=Button(v,text='Estoy a la izquierda',height=20,width=10)
botonIzq.grid(row=0,column=0)
botonDer=Button(v,text='Estoy a la derecha')
botonDer.grid(row=1,column=1)

v.mainloop()





