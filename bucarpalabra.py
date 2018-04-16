#########################################################
##Buscar una palabra y cuantas veces esta en mi archivo##
#########################################################

palabra=input("Ingresa la palabra que quieres buscar: ")

f=open("texto.txt","r")

texto=f.read()

palabras=texto.split() # "\n" "A"
 
print(palabras)

#Comenzado la busqueda 

if palabra in palabras:
	print("Se encontro la palabra: ",palabras.count(palabra),
		" veces en el archivo.")
else:
	print("La palabra no se encontro :(")