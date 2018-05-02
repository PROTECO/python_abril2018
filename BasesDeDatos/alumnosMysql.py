#################################
#Bases de datos
#################################

import mysql.connector


#Hacemos la conexión a la base de datos
conn = mysql.connector.connect(user= 'root', 
					 		 password= '',
					 		 host = 'localhost',
					 		 database = 'cursoPython')

#Y la crea

#La mayoría de las operaciones sobre las bases de datos se hacen utilizando
#un objeto que apunta a la base de datos y a través del cual podemos 
#ejecutar instrucciones similares al SQL estandar para obtener, insertar, actualizar o
#borrar algun dato.

cursor=conn.cursor()

print("\n\t\tBase de datos de los asistentes de Python Intermedio Semestral")

nombre=input("Ingresa el nombre del asistente: ")
promedio=float(input("¿Qué promedio tiene?"))

#Crear tablas
#Las operaciones se ejecutan a través del método execute del curso que
#declaramos

try:
	cursor.execute('''
		CREATE TABLE alumnos(id integer primary key AUTO_INCREMENT,nombre text,promedio float)''')
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
cursor.execute('SELECT * FROM alumnos ORDER BY promedio DESC')
consulta = cursor.fetchall()  

for row in consulta:
	print("Nombre: ",row[1],"Promedio: ",row[2])

#Cerrar la conexión
conn.close()