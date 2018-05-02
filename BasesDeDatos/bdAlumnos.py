#################################
#Bases de datos
#################################

import sqlite3

conn=sqlite3.connect('alumnos.db')  #Hacemos la conexión a la base de datos
#Y la crea

#La mayoría de las operaciones sobre las bases de datos se hacen utilizando
#un objeto que apunta a la base de datos y a través del cual podemos 
#ejecutar instrucciones similares al SQL estandar para obtener, insertar, actualizar o
#borrar algun dato.

cursor=conn.cursor()

print("\n\t\tBase de datos de los asistentes de python Intermedio")

nombre=input("Ingresa el nombre del asistente: ")
promedio=float(input("¿Qué promedio tiene?"))

#Crear tablas
#Las operaciones se ejecutan a través del método execute del curso que
#declaramos

try:
	cursor.execute('''
		CREATE TABLE alumnos(id integer primary key,nombre text,promedio float)''')
except:
	print("Saltándose la creación de la tabla porque ya existe! :D")

#Insertar cosas.
"""La forma recomendada es utilizar placeholders(marcadores de posición)
puesto que si armamos la cadena usando variables de python podemos correr
el riesgo de que nos hagan SQL injection"""

cursor.execute('INSERT INTO alumnos(nombre,promedio) VALUES("%s", "%f")'%(nombre,promedio))	

#Salvar cambios
conn.commit()	

#Ver todos los datos de la tabla

for row in conn.execute('SELECT * FROM alumnos ORDER BY promedio DESC'):
	print("Nombre: ",row[1],"Promedio: ",row[2])

#Cerrar la conexión
conn.close()