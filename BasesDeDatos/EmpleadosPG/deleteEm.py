import psycopg2

connect_str = "dbname='empleado' user='cursoPython'host='localhost' password='1234567890'"
conexion = psycopg2.connect(connect_str)
cur = conexion.cursor() #

#Para que me de solo dos decimales  coloco %.2f o donde va el 2, el número de decimales que quiera
rows= cur.execute("SELECT * FROM empleado")

rows= cur.fetchall()

for row in rows:
	print("ID: ",row[0],"\nNombre: ",row[1],row[2],"\nSueldo: ",row[3])

identificador=int(input("¿Qué registro quieres elminar?: "))

cur.execute("DELETE FROM empleado WHERE id=%i"%identificador)

conexion.commit()

print("Se ha eliminado el registro, con id: ",identificador)

conexion.close()
