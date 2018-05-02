import sqlite3 

conexion = sqlite3.connect('empleados.db') #Hacemos la conexion
cursor = conexion.cursor() #
try:
    cursor.execute('''CREATE TABLE empleado
                 (id integer primary key, nombre text, apellido text, sueldo real)''')
except:
    print ("Saltándose la creación de la tabla porque ya existe")

conexion.close()