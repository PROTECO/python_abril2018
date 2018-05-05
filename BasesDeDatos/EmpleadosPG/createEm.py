import psycopg2

connect_str = "dbname='empleado' user='cursoPython'host='localhost' password='1234567890'"
conexion = psycopg2.connect(connect_str)
cursor = conexion.cursor() #

try:
    cursor.execute('''CREATE TABLE empleado(
    id SERIAL PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL, sueldo REAL)''')
    conexion.commit()
except:
    print ("Saltándose la creación de la tabla porque ya existe")

conexion.close()
