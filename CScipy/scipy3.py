###################
##### Scipy #######
## Interpolación ##
###################

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,5*np.pi,20)
y = np.cos(x)

# interp1d(x,y,kind=)

lin = interp1d(x,y,kind='linear')
quad = interp1d(x,y,kind='quadratic')

# lin y quad no son valores aún

x2 = np.linspace(0,5*np.pi,100)

ylin = lin(x2)
yquad = quad(x2)

plt.plot(x,y,'o')
plt.plot(x2,ylin)
plt.plot(x2,yquad)
plt.legend(['datos','linear','cuadrátcio'])
plt.show()