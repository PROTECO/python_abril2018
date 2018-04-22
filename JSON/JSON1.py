############
## JSON ####
############

# JSON es un formato nuevo para el intercambio de datos
# Java Script Object Notation
# Está diseñado para ser neutral entre los lenguajes de programación
# A diferencia de pickle, con JSON el tipo de objetos que se puede almacenar es limitado

import json

nombre1 = dict(nombre = 'Luis Alberto', apellidos = ['Garrido','Mendoza'])
# diccionario = {'nombre': 'Luis Alberto', 'apellidos': ['Garrido','Mendoza']}

datos = dict(nombres = nombre1, trabajo = ['estudiante','python'], edad = 20)
print(datos)

J = json.dumps(datos)
print(J) # Como se almacena en formato JSON

D = json.loads(J)
print(D['trabajo'][1])
print(D['nombres']["apellidos"][1])

with open('ejemplo.txt','w') as archE:
	json.dump(datos,fp=archE,indent=4)

with open('ejemplo.txt') as archL:
	d = json.load(archL)

print(d['edad'])

