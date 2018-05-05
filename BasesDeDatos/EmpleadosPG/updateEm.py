import psycopg2

connect_str = "dbname='empleado' user='cursoPython'host='localhost' password='1234567890'"
conexion = psycopg2.connect(connect_str)
cur = conexion.cursor() #

#Para que me de solo dos decimales  coloco %.2f o donde va el 2, el número de decimales que quiera
rows= cur.execute("SELECT * FROM empleado")

rows= cur.fetchall()

for row in rows:
	print("ID: ",row[0],"\nNombre: ",row[1],row[2],"\nSueldo: ",row[3])

print("\nActualizando el nombre: ")

identificador=int(input("¿Qué id tiene?"))
nombre=input("Nuevo nombre: ")
cur.execute("UPDATE empleado SET nombre ='%s' WHERE id='%i'"%(nombre,identificador))

conexion.commit()


conexion.close()
