#Con este código podemos hacer diferentes funciones
#Y graficarlas en el mismo plano
import matplotlib
import numpy

x = numpy.linspace(-15,15,100) # 100 numeros linealmente espaciados
y = numpy.sin(x)/x # computando los valores de sin(x)/x

# hacer la grafica
matplotlib.plot(x,y) # sin(x)/x
matplotlib.plot(x,y,'co') # la misma funcion pero con puntos azules
#indicando con comas podemos graficar varias funciones
pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # graficar las 4 fincones