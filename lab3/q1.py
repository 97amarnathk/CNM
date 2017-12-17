import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, xList, yList):
    ans = 0
    for currX, currY in zip(xList, yList):
        prod = float(currY)
        for xi in xList:
            if xi != currX:
                prod*=(x-xi)/(currX-xi)
        ans += prod
    return ans

def numpyLagrange(x, xList, yList):
    y = []
    for xi in x:
        y.append(lagrange(xi, xList, yList))
    return np.array(y)

xList = [1.0, 4.0]
yList = [1.0, 2.0]
x = np.linspace(start = 0, stop = 5, num = 200)

plt.plot(x, numpyLagrange(x, xList, yList), 'k', label = r"$y = l_1(x)$")
plt.plot(xList, yList, 'ko')
plt.plot(x, x**(0.5), 'k--', label = r"$y = \sqrt{x}$")
plt.xlabel(r"x")
plt.ylabel(r"y")
plt.grid(True)
plt.legend()
plt.savefig("plots/q1.png", format = "png", dpi = 350)
