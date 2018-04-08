from tkinter import *

def hacerNada():
	pass
v=Tk()
v.wm_title("MENUS")
menubar=Menu(v)
#Con los menus de Tkinter podemos elaborar cualquier menu contextual
#Con funciones para cada uno de los labels
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo",command=hacerNada)
filemenu.add_command(label="Abrir",command=hacerNada)
filemenu.add_command(label="Guardar",command=hacerNada)
filemenu.add_command(label="Guardar Como",command=hacerNada)
filemenu.add_command(label="Cerrar",command=hacerNada)

filemenu.add_separator()
filemenu.add_command(label="Salir",command=v.quit)
menubar.add_cascade(label="Archivo",menu=filemenu)
###############################
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Deshacer",command=hacerNada)
editmenu.add_separator()
editmenu.add_command(label="Cortar",command=hacerNada)
editmenu.add_command(label="Copiar",command=hacerNada)
editmenu.add_command(label="Pegar",command=hacerNada)
editmenu.add_command(label="Borrar",command=hacerNada)
editmenu.add_command(label="Seleccionar Todo",command=hacerNada)
menubar.add_cascade(label="Editar",menu=editmenu)
################
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda...(F1)",command=hacerNada)
helpmenu.add_command(label="Acerca de",command=hacerNada)

menubar.add_cascade(label="Ayuda",menu=helpmenu)

v.config(menu=menubar)
v.mainloop()