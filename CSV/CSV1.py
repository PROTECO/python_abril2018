#########
## CSV ##
#########

# CSV -> Comma Separated Values
# Es el formato mas usado para importar y exportar datos de hojas de caluclo y bases de datos

import csv

with open('calificaciones.csv') as archivo:
	lectura = csv.reader(archivo)
	for fila in lectura:
		print(fila)

# Se crea una lista por fila

# Si los elementos no se separan con comas

with open('calificaciones2.csv') as archivo:
	lectura = csv.reader(archivo, delimiter=':')
	for fila in lectura:
		print(fila)


# Para escribir a un archivo

lista = [1,2,3,4,"hola"]

with  open('calificaciones.csv') as arch1 ,open('archivo.csv', 'w') as arch2:
	lectura = csv.reader(arch1)
	escritura = csv.writer(arch2,delimiter = ':')
	for fila in lectura:
		escritura.writerow(fila)

