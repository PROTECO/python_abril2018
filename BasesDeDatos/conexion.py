#Para instalar el conector: pip install mysql-connector

import mysql.connector

'''
con = mysql.connector.connect(user='****', password='*****',
                              host='127.0.0.1',
                              database='tasks')
'''
#Creamos la conexión a la base de datos
db = mysql.connector.connect(user= 'root', 
					 		 password= '',
					 		 host = 'localhost',
					 		 database = 'cursoPython')
#Creamos el cursor para movernos por la base
c = db.cursor()


c.execute('''INSERT INTO Asistentes (nombre,apPat,apMat,fechaNac,calificacion)
	VALUES("Julio","Martínez","Troncoso",'1997-07-07',9.9)
	''')
db.commit()

#c.execute('SELECT * FROM Asistentes')

#c.execute('DELETE FROM Asistentes WHERE numLista=4')
#c.execute('DELETE FROM Asistentes WHERE numLista=5')

#db.commit()
