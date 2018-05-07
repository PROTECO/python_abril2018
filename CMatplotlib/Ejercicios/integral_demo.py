"""
Grafica para demostrar que una integral es el area bajo una curva
Aunque es un programa simple ejemplifica varias cosass:

    * Un grafico de linea simple con color personalizado y ancho de la linea. 
    * Una region sombreada creado usando un parche Poligono. 
    * Una etiqueta de texto con la representacion mathtext. 
    * Etiquetas en los ejes
    * El uso de las espinas de los ejes para ocultar la parte superior y espina derecha. 
    * Colocacion  personalizado y etiquetas.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#La funcion a integrar
def func(x):
    return (x - 3) * (x - 5) * (x - 7) + 85


a, b = 2, 9 # limites de la integral
x = np.linspace(0, 10) #Espaciado entre valores
#Hacemos una relacion entre la funcion y un objeto
y = func(x)

fig, ax = plt.subplots() #Obtenemos subgraficas
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0) # y definimos los límites para 
#hacer la integral

# Hacer la regoin de la integral
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
#Utilizaremos el metodo de poligonos para dibujarla 
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

#Colocamos el texto que irá en el grafico
plt.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
         horizontalalignment='center', fontsize=20)

plt.figtext(0.9, 0.05, '$x$')
plt.figtext(0.1, 0.9, '$y$')

#Defimos si los topes estarán visibles
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

#Definimos si las esqunias estaran dibujadas
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([])
# enseñamos nuestro gráfico
plt.show()
