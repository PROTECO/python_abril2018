#!/usr/bin/env python3.4
import matplotlib.pyplot as plt
import numpy as np

#plt.plot(np.random.rand(10))
x1 = np.linspace(0.0,5.0)
x2 = np.linspace(0.0,2.0)

y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,'bo-')
plt.title('dos graficos')
plt.ylabel('Oscilacipn amortiguada')

plt.subplot(2,1,2)
plt.plot(x2,y2,'r*:')
plt.title('dos graficos')
plt.ylabel('no amortiguada')

plt.show()
