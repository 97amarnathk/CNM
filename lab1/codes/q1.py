import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-3, stop = 3, num=100)

y1 = x
y2 = np.exp(x)
y3 = np.log(x)
y4 = np.exp(-x)

plt.plot(x,y1,'k--',label=r'$y = x$')
plt.plot(x,y2,'k',label=r'$y = e^x$')
plt.plot(x,y3,'k:',label=r'$y = ln(x)$')
plt.xlabel(r'$x$')                                                                        
plt.ylabel(r'$y$')
plt.grid(True)
plt.legend()

plt.figure()

plt.plot(x,y2,'k--',label = r'$y = e^x$')
plt.plot(x,y4,'k',label = r'$y = e^{-x}$')
plt.grid(True)
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.show()
