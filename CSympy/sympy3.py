#########################
######## Sympy ##########
## Evaluación numérica ##
#########################

from sympy import *
# N(expresion, precisión)

expr = pi**2 - exp(3)/log(8)
pprint(expr) # Expresion sin evaluar
evaluado = N(expr)
print(evaluado)
evaluado = N(expr,3)
print(evaluado)


x,y,z = symbols('x,y,z')

expr2 = x**2 - log(z)/cos(y) + 3
pprint(expr2)

substituido = expr2.subs({x:3,y:2,z:4})
pprint(substituido)

evaluado2 = N(substituido)
print(evaluado2)

# Compilar expresiones
# Sympy sacrifica velocidad a cambio de precisión
# Para hacer una evaluación con mayor cantidad de datos
# es mejor compilar la expresión obtenida a una función
# que se pueda evaluar con numpy


expr3 = x**2 - y**3 + log(2*x-y+2)
pprint(expr3)

resultados = []
for i in range(10):
	resultados.append(N(expr3.subs({x:i,y:i}),8))

print(resultados)

# lambdify(argumentos, expr, "numpy")

import numpy as np

funcion = lambdify([x,y],expr3,"numpy")

valores = np.arange(10)
resultados = funcion(valores,valores)
print(resultados)

# %timeit [N(expr3.subs({x:i,y:i}),8) for i in range(1000)]
# valores = 1000
# %timeit funcion(valores,valores)
