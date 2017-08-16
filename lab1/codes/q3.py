import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, y0, a, u):
    return y0*np.exp(-a*(x-u)**2)

y0, a, u = 1, 1, 0
x = np.linspace(start = -10, stop = 10, num = 2000)

y01, y02, y03, y04 = -1, -0.5, 0.5, 1
plt.plot(x, gaussian(x, y01, a, u), 'k', linewidth = 0.5, label = r'$y_0 = -1$')
plt.plot(x, gaussian(x, y02, a, u), 'k', linewidth = 1, label = r'$y_0 = -0.5$')
plt.plot(x, gaussian(x, y03, a, u), 'k', linewidth = 1.5, label = r'$y_0 = 0.5$') 
plt.plot(x, gaussian(x, y04, a, u), 'k', linewidth = 2, label = r'$y_0 = 1$')     
plt.legend()
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.figure()

u1, u2, u3 = -1, 0, 1
plt.plot(x, gaussian(x, y0, a, u1), 'k', linewidth = 0.5, label = r'$\mu = -1$')
plt.plot(x, gaussian(x, y0, a, u2), 'k', linewidth = 1, label = r'$\mu = 0$')
plt.plot(x, gaussian(x, y0, a, u3), 'k', linewidth = 2, label = r'$\mu = 1$')
plt.legend()                                                                              
plt.grid(True)                                                                            
plt.xlabel(r'$x$')                                                                        
plt.ylabel(r'$y$')   

plt.figure()

a1, a2, a3 = 1, 4, 16
plt.plot(x, gaussian(x, y0, a1, u), 'k', linewidth=0.5, label =r'$a = 1$')
plt.plot(x, gaussian(x, y0, a2, u), 'k', linewidth=1, label =r'$a = 8$') 
plt.plot(x, gaussian(x, y0, a3, u), 'k', linewidth=2, label =r'$a = 64$') 
plt.legend()
plt.grid(True)                                                                            
plt.xlabel(r'$x$')                                                                        
plt.ylabel(r'$y$')

plt.figure()
y_gaussian = gaussian(x, y0, a, u)
y_lorentz = 1/(1+x**2)
plt.plot(x, y_gaussian, 'k', label = r'Gaussian')
plt.plot(x, y_lorentz, 'k--', label = r'Lorentz')
plt.legend()
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.figure()
                                                                                                                                                 
plt.plot(x, y_lorentz-y_gaussian, 'k')                                                                              
plt.grid(True)                                                                            
plt.xlabel(r'$x$')                                                                
plt.ylabel(r'$y$') 

plt.show()
