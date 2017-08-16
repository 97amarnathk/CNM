import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start = 0, stop = 3, num = 500)
y = x*np.log(x)
plt.plot(x, y, 'k')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.show()
