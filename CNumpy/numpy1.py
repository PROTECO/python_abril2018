##########################
######### Numpy ##########
## Creación de arreglos ##
##########################

import numpy as np

arr = np.arange(5)
# np.arange(inicio, final, intervalo, dtype=None)
# Similar a range()
print(arr,' Tipo:',type(arr))


# Convertir a lista
lista = arr.tolist()
print(lista, 'Tipo:' ,type(lista))


# Convertir a arreglo
lista = [3,4,5,6,7]
arr2 = np.array(lista)
print(arr2,'Tipo:', type(arr2))


# Arreglo de zeros
zeros = np.zeros(5)
print(zeros)


# Arreglo de unos
unos = np.ones(5)
print(unos)


#Arreglo de numeros aleatorios
aleatorios = np.random.uniform(size=5)
# Se puede especificar la distribución a usar
print(aleatorios)


# np.linspace(inicio, final, numero de elementos)
arrl = np.linspace(0,10,5)
print(arrl)


# Arreglo de dos dimensiones
arr2d = np.arange(16)
# Arreglo de 4 x 4
arr2d = arr2d.reshape((4,4))
print(arr2d)


arr2d2 = np.array([[1,2,3],[4,5,6]])
print(arr2d2)
print(arr2d2.shape)


# Arreglo de tres dimensiones
# Arreglo de 3 x 3 x 3
arr3d = np.arange(27).reshape((3,3,3))
print(arr3d)


# Indexación

a = np.arange(10)**2
print(a[2])
print(a[2:6])
print(a[:6:2])
a = np.arange(27).reshape([3,3,3])
print(a)
print(a[0,1,2])