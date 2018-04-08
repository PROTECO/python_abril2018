#Calculando el promedio

from tkinter import *
ventana=Tk()
label1=Label(ventana,text="Fisica")
label1.place(x=10,y=10)
e1= Entry(ventana,bd=5)
e1.place(x=85,y=10)
label2=Label(ventana,text="Curso Python")
label2.place(x=10,y=50)
e2=Entry(ventana,bd=5)
e2.place(x=85,y=50)
label3=Label(ventana,text="PROMEDIO")
label3.place(x=10,y=150)
e3=Entry(ventana,bd=5)
e3.place(x=85,y=150)

def calculaProm():
	"""
	Funcion que calcula el promedio de Física y Curso Python
	el método delete me permite limpiar los cuadros de texto
	el método get me permite obtener lo que hay en un cuadro		
	"""
	e3.delete(0,len(e3.get()))
	e3.insert(0,str((int(e1.get())+int(e2.get()))/2))


boton= Button(ventana,text="Tu promedio es: ",command=calculaProm)
boton.place(x=100,y=100)
ventana.geometry("300x250")
ventana.resizable(width=False,height=False)
ventana.title("Calcula tu promedio")
ventana.mainloop()




