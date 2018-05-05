import psycopg2

connect_str = "dbname='empleado' user='cursoPython'host='localhost' password='1234567890'"
conexion = psycopg2.connect(connect_str)
cur = conexion.cursor() #

rows= cur.execute("SELECT * FROM empleado")

rows= cur.fetchall()

for row in rows:
	print("ID: ",row[0],"\nNombre: ",row[1],row[2],"\nSueldo: ",row[3])
conexion.close()
