##################
## Archivos XML ##
##################

# Parseo -> Dividir un archivo o entrada en pedazos de datos
# XML es un lenguaje basado en etiquetas para definir información de forma estructurada
# Normalmente es utilizado para definir documentos u otros datos en la Web

# Método DOM

import xml.dom.minidom
from xml.dom.minidom import Node
# Con este método recorremos un arbol de objetos, las etiquetas funcionan como nodos


#Cargamos el documento 
arbol1 = xml.dom.minidom.parse("libros.xml")
ids = []
for nodoBook in arbol1.getElementsByTagName("book"):
	ids.append(nodoBook.getAttribute("id"))
# Vamos iterando por todos los nodos 'book' y guardamos sus ids

print(ids)

autores = []
for nodeAuthor in arbol1.getElementsByTagName("author"):
	for nodoHijo in nodeAuthor.childNodes:
		autores.append(nodoHijo.data)
#Iteramos por los nodos hijos de 'author' que vendría siendo el texto
#Guardamos la información del nodo hijo

print(autores)
print(len(ids),len(autores))

# zip -> junta dos iteradores un un solo iterador
z = zip(ids,autores)

print(z)
print(next(z))

for i,j in zip(ids,autores):
	print(i,"->",j)

# Método ElementTree

# También funciona recorriendo un arbol de objetos, se considera más sencillo
from xml.etree.ElementTree import parse

arbol2 = parse("libros.xml")
D = {}
for nodo in arbol2.findall("book"):
	ID = nodo.attrib["id"]
	for titulo in nodo.findall("title"): # Se debe ejecutar en nodo "book"
		D[ID] = titulo.text

for llave in D:
	print(llave,"->",D[llave])