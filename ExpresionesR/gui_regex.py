from tkinter import *
import re

# Este script despliega una ventana en la que se puede colocar un patrón
# y la dirección de un archivo, al apretar el boton se realizara una búsqueda
# en el texto mostrando todos los matchs en una lista.

principal = Tk()
principal.title("Expresiones Regulares")
principal.resizable(width="False",height="False")
principal.geometry("251x195")


e1 = Entry(principal)
e2 = Entry(principal)
l1 = Label(principal, text="Patrón :")
l2 = Label(principal, text="Archivo :")
b = Button(principal, bg="orange")
scrollbar = Scrollbar(principal)
lista = Listbox(principal)


l1.grid(row = 0, column = 0, sticky = W)
l2.grid(row = 1, column = 0, sticky = W)
e1.grid(row = 0, column = 1, sticky = EW)
e2.grid(row = 1, column = 1, sticky = EW)
b.grid(row=0,column=2,rowspan = 2,columnspan = 2,sticky=NSEW)
lista.grid(row=2,column=0,rowspan=3,columnspan=3,sticky=NSEW)
scrollbar.grid(row = 2, column = 3, rowspan = 3, sticky = NSEW)


principal.mainloop()