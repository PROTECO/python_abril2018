#########################
######## Sympy ##########
####### Cálculo #########
#########################

from sympy import *

# Derivación

# diff(expresion,
#	   valor con respecto al que se deriva,
#	   orden de derivada)

x,y = symbols('x y')

expr = 3*y*x**3 + y**3
pprint(expr)

pprint(diff(expr,x))
pprint(diff(expr,x,2))
pprint(diff(expr,y))
pprint(diff(expr,y,2))
pprint(diff(expr,x,2,y,1))

# Límites

# limit(expresion,
#		variable,
#		a donde tiende,
#		por que lado)
expr2 = 1/x
pprint(expr2)
pprint(limit(expr2,x,3))
pprint(limit(expr2,x,0))
pprint(limit(expr2,x,0,'-'))
pprint(limit(expr2,x,0,'+'))
pprint(limit(expr2,x,oo))

# Integrales

# integrate(expr, (variable,lim inferior, lim superior))

pprint(integrate(cos(x),x))
print(integrate(cos(x),(x,0,pi/2)))

expr2 = x + y
pprint(x+y)

pprint(integrate(expr2,x))
pprint(integrate(expr2,x,y))
pprint(integrate(expr2,(x,0,2),(y,-1,1)))

# Integral
# expresion con integral

pprint(Integral(sin(x),x))
pprint(Integral(sin(x),(x,-10,1)))

integral = Integral(sin(x),(x,-10,1))
pprint(integral)
resuelta = integral.doit()
print(resuelta)
print(N(resuelta))
