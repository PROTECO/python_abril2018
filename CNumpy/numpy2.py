##############################
########### Numpy ############
## Operacicones de arreglos ##
##############################

import numpy as np

x = np.array([3,4,2,5])
y = np.array([2,1,2,1])
print(x+y,x-y,x*y)

# Las operaciones son elemento por elemento
# broadcasting

print(x * 2, x + 1, x**2)

# Se permite hacer operaciones con arreglos del
# mismo tamaño a con escalares

# z = np.array([1,2,3])
# z + x 
# Esto no daría un error

x = np.arange(-2*np.pi,2*np.pi,np.pi/2)
print(np.sin(x))

y = np.round(np.sin(x))
print(y)

matriz1 = np.arange(9).reshape((3,3))

matriz2 = np.ones(9).reshape((3,3))*2

print(matriz1)
print(matriz2)

# producto elemento por elemento
print(matriz1*matriz2)


# producto matricial
print(matriz1.dot(matriz2))

# diagonal
print(matriz1.diagonal())

# transpuesta
print(matriz1.transpose())

z = np.array([[2,5,3],[6,4,3],[9,7,6]])
# determinante
print(np.linalg.det(z))

# inversa
print(np.linalg.inv(z))

# Resolución de sistema de ecuaciones

a = np.array([[3, 6, -5],
			 [1, -3, 2],
			 [5, -1, 4]])


b = np.array([12, -2, 10])

x = np.linalg.inv(a).dot(b)
print(x)

# Booleanos

numeros = np.arange(-10,10)
print(numeros)
print(numeros > 0)

indices = numeros > 0

print(numeros[indices])

indices1 = numeros < 5
print(numeros[indices & indices1])

indices2 = numeros < -5
print(numeros[indices | indices2])
