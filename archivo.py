############
##Archivos##
############

archivo=open("texto.txt","r+")

print("Nombre del archivo: ",archivo.name)
print("Modo de apertura: ",archivo.mode)

texto=archivo.read() #readlines
print(texto)
print(type(texto)) #String

textonuevo=input("Ingrese el texto para escribir: ")

archivo.write("\n"+textonuevo)

print(texto)