#########
#Gesturas de posición
#Pack

#Pack: Permitir colocar objetos en la ventana en orden
#descendente, el ancho se ajustará al tamaño del elemento
#con mayor tamaño
#Importamos todo lo que contiene el modulo tkinter
from tkinter  import *
#Creamos un objeto de tipo ventana
ventana = Tk()
#side: Me permite acomodar los elementos uno abajo de otro
#o uno a la izquierda de otro
#fill: Rellena el elemento en el eje x
#expand: Hace crecer al elemento junto con la ventana
Button(ventana,text="Top").pack(side=TOP,fill=X,expand=YES)
Button(ventana,text="Centro").pack(side=TOP,fill=X,expand=NO)
Button(ventana,text="Final").pack(side=TOP,fill=X,expand=NO)

Button(ventana,text="Izquierda").pack(side=LEFT,fill=Y,expand=YES)
Button(ventana,text="Centrado").pack(side=LEFT,fill=X)
Button(ventana,text="Derecha").pack(side=LEFT,fill=X)

ventana.mainloop()








