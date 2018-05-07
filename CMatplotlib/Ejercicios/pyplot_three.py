import numpy as np
import matplotlib.pyplot as plt

# uniformemente muestreada tiempo en intervalos de 200 ms
t = np.arange(0., 5., 0.2)

# guiones rojos, cuadrados azules y triangulos verdes
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
