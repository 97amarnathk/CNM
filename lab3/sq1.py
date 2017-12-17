import numpy as np
import matplotlib.pyplot as plt
import splines

xList = [1.0, 2.0, 3.0, 4.0]
yList = [1.0, 1/2.0, 1/3.0, 1/4.0]

ansList, splineRange = splines.getSplines(xList, yList)

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
#plot y=1/x
plt.plot(splineRange, 1/splineRange, 'k',linewidth = 2, label = r"$y = \frac{1}{x}$")
#plot the linear interpolation
plt.plot(xList, yList, 'k--', linewidth = 1, label = r"linear")
#plot the spline interpolation
plt.plot(splineRange, ansList, 'k', linewidth = 1,label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/sq1a.png", format = "png", dpi = 350)
plt.close()

#plot the errors
plt.plot(splineRange, np.abs(1/splineRange - ansList), 'k')
plt.xlabel(r"$x$")
plt.ylabel(r"error")
plt.grid(True)
plt.legend()
plt.savefig("plots/sq1b.png", format = "png", dpi = 350)
plt.close()
