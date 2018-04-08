"""
6. Escriba un scripts Python para contar el número de números pares e impares de una serie de números. 
Números de muestra : números = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Producto esperado :
Número de números pares: 5
Número de números impares: 4
"""
listaNums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
contPares=0
contImpares=0
for numero in listaNums:
	if numero%2==0:
		contPares+=1
	else:
		contImpares+=1

print('Número de números pares: ',contPares)
print('Número de números impares: ',contImpares)



