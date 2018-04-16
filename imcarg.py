######################
##IMC con Modolo SYS##
######################

import sys

print(len(sys.argv))

if len(sys.argv)<=2:
	print("Te hace falta parametros!")
	exit(1)

while True:
	peso=float(sys.argv[1])
	altura=float(sys.argv[2])
	IMC=peso/(altura*altura)

	if IMC<18:
		print("Infrapeso")
	elif IMC<25:
		print("peso saludable :)")
	else:
		print("Bajale a los tacos")

	a=input('Escribe "salir" para terminar')
	if a=='salir':
		break