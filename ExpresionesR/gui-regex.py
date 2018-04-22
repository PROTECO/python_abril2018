from tkinter import *
import re

# Se puede hacer el código junto a una terminal para ir viendo el 
# funcionamiento de las funciones nuevas

# Este script despliega una ventana en la que se puede colocar un patrón
# y la dirección de un archivo, al apretar el boton se realizara una búsqueda
# en el texto mostrando todos los matchs en una lista.

principal = Tk()
principal.title("Expresiones Regulares")
principal.resizable(width="False",height="False")
principal.geometry("251x195")

def busqueda():
	lista.delete(0,END) # Borramos todo lo que haya en la lista
	patron = e1.get()
	path = e2.get()
	p = re.compile(patron) # Compilamos el patron
	try:
		archivo = open(path)
		lineas = archivo.readlines() # Creamos lista de lineas
		texto = "".join(lineas)  # Juntamos elementos de lista en un solo string
		texto.replace("\n"," ") # Borramos saltos de linea
		texto.replace("\r"," ") 
		for match in p.findall(texto):
			lista.insert(END,match) # Agregamos los match a la lista
		archivo.close()
	except:
		lista.insert(END,"Archivo no encontrado") # En caso de que el archivo no se encuentre


e1 = Entry(principal)
e2 = Entry(principal)
l1 = Label(principal, text="Patrón :")
l2 = Label(principal, text="Archivo :")
b = Button(principal, bg="orange", command = busqueda)
scrollbar = Scrollbar(principal)
lista = Listbox(principal, yscrollcommand = scrollbar.set)
scrollbar.config(command = lista.yview)

l1.grid(row = 0, column = 0, sticky = W)
l2.grid(row = 1, column = 0, sticky = W)
e1.grid(row = 0, column = 1, sticky = EW)
e2.grid(row = 1, column = 1, sticky = EW)
b.grid(row=0,column=2,rowspan = 2,columnspan = 2,sticky=NSEW)
lista.grid(row=2,column=0,rowspan=3,columnspan=3,sticky=NSEW)
scrollbar.grid(row = 2, column = 3, rowspan = 3, sticky = NSEW)


principal.mainloop()