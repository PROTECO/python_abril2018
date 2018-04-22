#Almacenar los datos de un sensor en un diccionario

import re


patron = "(\w+) = (\d+\.?\d+)"
texto = """Temperatura = 30.5 °C,
			Presión = 78403 Pa, 
			Altura = 50.3 m,
			Tiempo = 45.832 s """

diccionario = {}
for i in re.finditer(patron,texto):
	diccionario[i.group(1)] = float(i.group(2))

print(diccionario)
print(diccionario['Temperatura'])