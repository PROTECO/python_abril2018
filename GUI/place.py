#########
#Gesturas de posición
#GRID

from tkinter import *
v=Tk()

botonIzq=Button(v,text='Estoy a la izquierda').place(x=0,y=0)
botonDer=Button(v,text='Estoy a la derecha').place(x=100,y=0)
botonRand=Button(v,text='No se donde estoy').place(x=200,y=300)

v.mainloop()