import numpy as np
import matplotlib.pyplot as plt

xList = [0, 1, 2, 3, 4, 5, 6]
yList = [2, 2.1592, 3.1697, 5.4332, 9.1411, 14.407, 21.303]

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
plt.plot(xList, yList, 'k-')
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q4.png", format = "png", dpi = 350)
plt.close()
