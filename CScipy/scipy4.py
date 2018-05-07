#################
##### Scipy #####
## Estadística ##
#################

import numpy as np
import matplotlib.pyplot as plt

# Numpy nos da funciones básicas
x = np.random.randn(1000)
mean = x.mean() #Media
std = x.std() # Desv Estadar
var = x.var() # Varianza

from scipy.stats import norm
# distribución normal

x = np.linspace(-5,5,1000)
# loc es media y scale es desviación estandar que vamos a usar
distr = norm(loc = 0, scale = 1)

# pdf -> probability density functions
# cdf -> cumulative distribution functions
# rvs -> random variable samples

pdf = distr.pdf(x)
cdf = distr.cdf(x)
muestra = distr.rvs(10000)

print(pdf)
print(cdf)
plt.hist(muestra,bins = 100)
plt.show()