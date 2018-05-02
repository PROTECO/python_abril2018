import sqlite3

conexion = sqlite3.connect("empleados.db")
cursor = conexion.cursor()
while True:
    query = input("Query: ")
    cursor.execute(query)
    conexion.commit()
    for row in cursor.fetchall():
        print (row)