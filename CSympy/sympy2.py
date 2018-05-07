#################################
########### Sympy ###############
## Manipulación de expresiones ##
#################################

from sympy import *

a = Symbol('a', positive = True)
z = Symbol('z') #complejo por default
x = Symbol('x', real = True)
# Especificar caracteristicas sirve al simplificar

expr1 = pi**2 - 9
print(expr1.is_positive)

expr2 = a*2 + 3
print(expr2.is_positive)
# Ventajas de especificar caracteristicacs del símbolo

# Substituciones

x,y,z = symbols('x:z')

expr3 = cos(x)

print(expr3.subs(x,2),expr3.subs(x,0)) # subs(antes, despues)


expr4 = exp(y) * cos(x) - log(z)
pprint(expr4.subs({y:2,x:pi,z:1}))
# {antes:despues}



# Simplificación de expresiones

pprint(simplify(cos(log(a**2))*tan(log(a**2))))

# radsimp() -> simplificación con raizes cuadradas
# trigsimp() -> simplificación a combinación de funciones trigonométricas
# cancel() -> quita factores en comun
# together() -> junta a un solo denominador
# apart() -> fracciones parciales

# Expanción de expresiones

# expand_power_base()
# expand_power_exp()
# expand_log()
# expand_complex()
# expand_trig()

# Igualdad de expresiones

print(x**2 == x*x)
print((x-a)**2 == (x**2 - a**2))
