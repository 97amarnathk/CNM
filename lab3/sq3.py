import numpy as np
import matplotlib.pyplot as plt
import splines

xList = [-0.5, 0.0, 0.25, 1.0]
yList = [0.731531, 1.0, 1.2684, 1.718282]

ansList, splineRange = splines.getSplines(xList, yList)

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
#plot the linear interpolation
plt.plot(xList, yList, 'k--', label = r"piecewise linear")
#plot the spline interpolation
plt.plot(splineRange, ansList, 'k',label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/sq3a.png", format = "png", dpi = 350)
plt.close()

#plot exp(x) - x**3
f = np.exp(splineRange) - splineRange**3
plt.plot(splineRange, f, 'k',label = r"$y = e^x - x^3$")
plt.plot(splineRange, ansList, 'k--', label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/sq3b.png", format = "png", dpi = 350)
plt.close()

#plot error
plt.plot(splineRange, np.abs(ansList - f), 'k')
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"error")
plt.savefig("plots/sq3c.png", format = "png", dpi = 350)
plt.close()
