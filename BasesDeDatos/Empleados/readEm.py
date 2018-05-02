import sqlite3

conexion=sqlite3.connect("empleados.db")

cursor= conexion.cursor()

for row in conexion.execute('SELECT * FROM empleado'):
	print(row)
conexion.close()