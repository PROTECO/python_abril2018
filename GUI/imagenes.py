####
# Imágenes con tkinter
####

from tkinter import *

#tkinter únicamente soporta imagenes en formato .png y .gift
#si queremos imagenes .jpg hay que importar el módulo PIL

v= Tk()

#Se debe crear una variable que guarde la imagen
imagen=PhotoImage(file='python.png')
imagen = imagen.subsample(10)
l1=Label(v,image=imagen).pack(side=RIGHT)
texto='''PAra utilizar imagenes con python y tkinter se deben utilizar 
los formatos PNG o GIF, o utilizar el módulo JPG
'''

l2=Label(v, justify=LEFT,text=texto).pack(side=LEFT)

v.mainloop()