import numpy as np
import matplotlib.pyplot as plt
import splines

xList = [1.0, 2.0, 3.0, 4.0, 5.0]
yList = [3.0, 1.0, 2.0, 3.0, 2.0]

ansList, splineRange = splines.getSplines(xList, yList)

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
#plot the spline interpolation
plt.plot(splineRange, ansList, 'k', linewidth = 1,label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q3a.png", format = "png", dpi = 350)
plt.close()
print " "

xList = [0.0, 0.5, 1.0, 2.0, 3.0]
yList = [0, 0.25, 1.0, -1.0, -1.0]

ansList, splineRange = splines.getSplines(xList, yList)

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
#plot the spline interpolation
plt.plot(splineRange, ansList, 'k', linewidth = 1,label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q3b.png", format = "png", dpi = 350)
plt.close()

print " "

xList = [0.0, 1.0, 2.0, 2.5, 3.0, 4.0]
yList = [1.4, 0.6, 1.0, 0.65, 0.6, 1.0]

ansList, splineRange = splines.getSplines(xList, yList)

#plot the sample points
plt.plot(xList, yList, 'ko', label = "data points")
#plot the spline interpolation
plt.plot(splineRange, ansList, 'k', linewidth = 1,label = r"spline")
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q3c.png", format = "png", dpi = 350)
plt.close()
