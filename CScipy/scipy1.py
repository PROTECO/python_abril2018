#################
##### Scipy #####
## Integración ##
#################

import numpy as np

# Integración analítica

# Necesitamos conocer la función a integrar
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definimos función a integrar
def func(x):
	return np.cos(3*x+2)

# quad(funcion, intervalo menor, intervalo mayor)

solucion = quad(func,0,3)
print(solucion) # solucion = (solucion, error)


# Integración numérica

# Se tiene datos en lugar de una función

from scipy.integrate import quad, trapz

x = np.sort(np.random.randn(200) * 4 + 4).clip(0,5)
# disminuuir el numero de elementos para ver la variación de resultados

y = func(x)

solucionfun = quad(func,0,3)
soluciondat = trapz(y,x=x)
print(solucionfun)
print(soluciondat)