##############
##Modolo SYS##
##############

import sys

#print(sys.version)
#print(sys.platform)

#print(sys.argv) #Parametros de la linea
				#de comandos
numeracion=0

for argumento in sys.argv:
	print("prametro %i: es: %s"%(numeracion,argumento))
	numeracion+=1