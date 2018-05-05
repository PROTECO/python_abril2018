import psycopg2

connect_str = "dbname='empleado' user='cursoPython'host='localhost' password='1234567890'"
conexion = psycopg2.connect(connect_str)
cursor = conexion.cursor() #

print("Base de datos de los empleados \n")

identificador = int(input("Ingresa el id: "))
name = input("Ingresa el nombre: ")
ap = input("Ingresa el apellido: ")
sldo = float(input("Ingresa el sueldo: $ "))


cursor.execute("""INSERT INTO empleado (id,nombre,apellido,sueldo) VALUES(%s,%s,%s,%s)""",(identificador,name,ap,sldo))

#cursor.execute("INSERT INTO empleado VALUES(2,'Julio','Martínez',100.00)")


conexion.commit()
