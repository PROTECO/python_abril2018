##################
##### Scipy ######
## Optimización ##
##################

import numpy as np

# Modelado de datos

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

"""def func(x,a,b):
	return a*x + b

x = np.linspace(0,10,100)
y = func(x,2,3)

yn = y + 0.9 * np.random.normal(size=len(x))


valores, var = curve_fit(func, x, yn)

print(valores) # a,b obtenidos
print(var) # la diagonal principal de var son las varianzas de los valores

plt.plot(x,y)
plt.plot(x,yn,'.')
plt.plot(x,func(x,valores[0],valores[1]))
plt.legend(['función','datos','aproximación'])
plt.show()


def func(x,a,b,c):
	return (-x)**2 + b**2 - a + x*c

x = np.linspace(-3,3,60)
y = func(x,-2,2,1)

yn = y + 0.2*np.random.normal(size=len(x))

valores,var = curve_fit(func,x,yn)
a,b,c = valores

plt.plot(x,y)
plt.plot(x,yn,'.')
plt.plot(x,func(x,a,b,c))
plt.legend(['función','datos','aproximación'])
plt.show()

"""
def func(x, a0, b0, c0, a1, b1,c1):
	return a0*np.exp(-(x - b0) ** 2/(2 * c0 ** 2))\
		+ a1 * np.exp(-(x - b1) ** 2/(2 * c1 ** 2))

x = np.linspace(0,20,200)
y = func(x,1,3,1,-2,15,0.5)

yn = y + 0.2*np.random.normal(size=len(x))

# Al ser una función compleja, se recomienda usar una suposición


suposicion = [1,3,1,-1,15,1]

valores,var = curve_fit(func,x,yn)
a0,b0,c0,a1,b1,c1 = valores

plt.plot(x,y)
plt.plot(x,yn,'.')
plt.plot(x,func(x,a0,b0,c0,a1,b1,c1))
plt.show()


# Solución de funcion
# fsolve(funcion, punto de referencia)
