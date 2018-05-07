##############################
########### Numpy ############
####### Vectorización ########
##############################

import numpy as np

def funcion (a,b):
	if a > b:
		return a-b
	else:
		return a+b

print(funcion(3,4),funcion(4,3))

x = np.array([2,3,5,8,5,3])
y = np.array([7,5,3,5,2,4])

# print(funcion(x,y)) 
# Esto mandaría un error

vfuncion = np.vectorize(funcion)
print(vfuncion(x,y))