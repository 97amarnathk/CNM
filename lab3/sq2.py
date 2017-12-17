import numpy as np
import matplotlib.pyplot as plt
import splines

xList = [0.0, 1.0, 2.0, 2.5, 3.0, 3.5, 4.0]
yList = [2.5, 0.5, 0.5, 1.5, 1.5, 1.125, 4.0]

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
plt.savefig("plots/sq2.png", format = "png", dpi = 350)
plt.close()
