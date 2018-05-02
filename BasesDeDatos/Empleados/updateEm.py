import sqlite3


conexion=sqlite3.connect("empleados.db")

cursor= conexion.cursor()
#Para que me de solo dos decimales  coloco %.2f o donde va el 2, el número de decimales que quiera
for row in conexion.execute('SELECT * FROM empleado'):
	print(row)

print("\nActualizando el nombre: ")
identificador=int(input("¿Qué id tiene?"))
nombre=input("Nuevo nombre: ")
cursor.execute("UPDATE empleado SET nombre ='%s' WHERE id='%i'"%(nombre,identificador))

conexion.commit()


conexion.close()
