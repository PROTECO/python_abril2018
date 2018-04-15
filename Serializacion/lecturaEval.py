############
## eval ####
############

#eval permite convertir una cadena de texto en una expresión

x = eval('4+4')
print(x)

y = eval('[3,5,3,6]')
print(y[2])

D = eval(open('diccionario.txt').read())
#Podemos guardar un diccionario en un archivo y recuperarlo
#en otro script con eval

#Para crear multiples objetos se puede hacer
# D,L = eval('{...},[...]')

print(D['Jorge'])

# exec permite convertir una cadena de texto en una declaración

exec('z = 4+4')
print(z)