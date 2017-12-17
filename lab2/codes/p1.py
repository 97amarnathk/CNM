import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start = -1.5, stop = 1.5, num = 2000)
plt.plot(x, x**4, 'k', label = r"$x^4$")
plt.plot(x, x+1, 'k--', label = r"$x+1$")
plt.grid(True)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("p10.png", format = "png", dpi = 350)
