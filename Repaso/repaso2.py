# Escriba un programa en Python para convertir las temperaturas de y hacia Celsius y Fahrenheit. 
# Fórmula: C / 5 = F-32/9 [donde C = temperatura en grados Celsius y F = temperatura en Fahrenheit]
# Salida esperada:
# 60 ° C es 140 en Fahrenheit
# 45 ° F es 7 en Celsius
#################################################################################################
c=float(input("Dame la temperatura en grados Celsius: "))
f=float(input("Dame la temperatura en grados Fahrenheit: "))
print("%.2f ° C es %.2f en Fahrenheit" % (c,(c*9/5)+32)) #para solo la parte entera
print("%.2f ° F es %.2f en Celsius" % (f,(f-32)*(5/9)))  #cambiar %,.2f por %d