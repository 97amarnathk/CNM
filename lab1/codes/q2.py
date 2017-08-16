import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(start = -np.pi, stop = np.pi, num = 100000)
k1, k2, k3 = 1, 8, 64
y1, y2, y3 = np.sin(k1*x), np.sin(k2*x), np.sin(k3*x)
plt.plot(x, y1, 'k', label = r'$y = sin(x)$', linewidth = 3)
plt.plot(x, y2, 'k', label = r'$y = sin(8\cdot x)$', linewidth = 1.5)
plt.plot(x, y3, 'k', label = r'$y = sin(64\cdot x)$', linewidth = 0.5)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.grid(True)

plt.figure()
y4 = np.sin(k1*x)**2
plt.plot(x, y1, 'k', label = r'$y = sin(x)$')
plt.plot(x, y4, 'k--', label = r'$y = sin^2(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.grid(True)
plt.show()
