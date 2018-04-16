#########################
##Copiar archivo a otro##
#########################

origen=open(input("Archivo origen: "),"r+")
destino=open(input("Archivo destino: "),"w")

for linea in origen.readlines():
	destino.write(linea)