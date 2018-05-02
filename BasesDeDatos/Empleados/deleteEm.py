
import sqlite3


conexion=sqlite3.connect("empleados.db")

cursor= conexion.cursor()
#Para que me de solo dos decimales  coloco %.2f o donde va el 2, el número de decimales que quiera

for row in conexion.execute('SELECT * FROM empleado'):
	print(row)
identificador=int(input("¿Qué registro quieres elminar?: "))

cursor.execute("DELETE FROM empleado WHERE id=%i"%identificador)

conexion.commit()

print("Se ha eliminado el registro, con id: ",identificador)

conexion.close()