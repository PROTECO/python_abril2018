import matplotlib.pyplot as plt
#Podemos graficar más de un intervalo
#El "ro" significan circulos rojos
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#Estos valores irán en donde se crucen los ejes
plt.axis([0, 6, 0, 20])
#Terminamos de enseñar nuestra gráfica
plt.show()
