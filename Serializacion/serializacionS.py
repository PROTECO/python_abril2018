###############################
## Serialización con shelve  ##
###############################

import shelve

# shelve permite guardar objetos serializados con pickle con llaves
# Es muy parecido a los diccionarios

#Serializar

db = shelve.open('baseDatos')

# Se almacenan de igual forma que elementos de un diccionario
# Es necesario que las llaves seas de tipo string
db['calificaciones'] = {'Julio':8,'Ana':9,'Jose':9,'Luis':8,'Jorge':9,'Pedro':10,'Mariana':10}
db['valores'] = [1,2,3,4]
db['imaginarios'] = (1+2j,2-3j)
db['booleano'] = True

db.close()


#Recrear objetos

DB = shelve.open('baseDatos')

print(len(DB))
print(list(DB.keys()))
print(list(DB.items()))
print(DB['valores'])

DB.close()
