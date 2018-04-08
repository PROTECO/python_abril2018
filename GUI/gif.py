##################
# GIFs en tkinter
##################

from tkinter import *

root = Tk()
# Con esta linea  puedes calcular cuantos frames tiene el gif si tiene más de 200, aumentar el range()
#frames = [print(PhotoImage(file='archivo.gif',format = 'gif -index %i' %(i))) for i in range(200)]
#maxframes= ... usar esta variable para el script
#Entre más frames más tarda en cargarse el programa, este tiene 111 frames

frames = [PhotoImage(file='catslap.gif',format = 'gif -index %i' %(i)) for i in range(111)]

def update(ind):
	"""Esta funcion se encarga de actualizar los frames"""
	if ind==110: #Si llegamos al último frame que carge el primero para ciclar el gif
		ind=0
	frame = frames[ind] #aqui agarramos el frame de la lista
	ind += 1
	label.configure(image=frame)
	root.after(1000, update, ind)
#Creamos una ventana
label = Label(root)
label.pack()
root.title("Ejemplo gif")
#Y ligamos a la funcion update
root.after(0, update, 0)
root.mainloop()