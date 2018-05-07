#############################
########### Sympy ###########
## Creación de expresiones ##
#############################

#%load_ext sympy.interactive.ipythonprinting

from sympy import *


# Sympy utiliza su propia clase de numeros


print(3,Integer(3)) #Objeto sympy de timpo Integer
print(type(Integer(3)))

#Convertir a objetos de sympy
print(3.2,S(3.2))
print(type(S(3.2)))

a = Integer(7) + Integer(4)
b = Integer(8) - Integer(2)
c = Integer(4) * Integer(4)
d = Integer(3) / Integer(12)
e = Integer(12) % 5 
# El resultado de la operación entre objetos de
# sympy y numeros de Python, es un objeto de sympy

print(a,b,c,d,e,sep='   ')

# descomposición de factores
print(factorint(42))
# minimo comun multiplo y maximo comun divisor
print(lcm(15,20),gcd(15,20))

# Calculo de hipotenusa

a = S(1) / 2
b = S(2) / 3
c = sqrt(a**2 + b**2)
print(c)


# Símbolos

z = Symbol('z')
a = Symbol('a')
pprint(a**2 + z) #print - pprint

# pprint -> pretty print

x,y,z = symbols('x y z')
#x,y,z = symbols('x, y, z')
pprint(x+y**2+z**3)

a,b,c,f,g = symbols('a:c, f:g')
pprint(a+b+c+f+g)

x0,x1,x2,x3 = symbols('x:4')
pprint(x0 - x1 + x2 - x3)

pprint(x + 2*y + x -3*y)

print(cos(3), cos(0),end='\n\n\n')

pprint(cos(x)**2 + exp(atanh(y))/log(z))
