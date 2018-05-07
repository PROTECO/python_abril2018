##############################
######## Sympy ###############
## Resolución de ecuaciones ##
##############################

from sympy import *

# solve(expr, variable a resolver)

# solve regresa una lista con las soluciones
# si el conjunto de soluciones no es finito regresa []
# si no hay solución, regresa []
# si la funcion es periodica, regresa solo una solución

x = Symbol('x')

expr = x**2 + x - 3
pprint(solve(expr,x))

x = Symbol('x', real=True)
z = Symbol('z')
pprint(solve(z**2 + 1, z))
pprint(solve(x**2 + 1, x))

y = Symbol('y')

expr2 = x**2 + y**2 - z
pprint(expr2)
pprint(solve(expr2,x))
pprint(solve(expr2,x,y)) # devuelve el resultado en lista de diccionarios
# util para hacer subs(resultado)

resultados = solve(expr2,x,y)

expr3 = x + 4 * log(x)

for resultado in resultados: # iterando sobre lista de diccionarios
	pprint(expr3.subs(resultado))

# Resolución de sistema de ecuaciones

#solve(
#	   [lista con ecuaciones igualadas a 0],
#		variable1,variable2,....,
#		dict=True)

solucion=solve([3*x + y - 13, x - y - 3], x, y, dict = True)

pprint(solucion)