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

xList1 = [0.82, 0.83]
yList1 = [2.270500, 2.293319]
xList2 = [0.82, 0.83, 0.84]
yList2 = [2.270500, 2.293319, 2.316367]
x = np.linspace(start = -1, stop = 2, num = 200)

#Function
plt.plot(x, np.exp(x), 'k', label = r"$y = e^x$")
plt.plot(x, numpyLagrange(x, xList1, yList1), 'k:', label = r"$y = l_1(x)$")
plt.plot(x, numpyLagrange(x, xList2, yList2), 'k--', label = r"$y = l_2(x)$")
plt.xlabel(r"x")
plt.ylabel(r"y")
plt.grid(True)
plt.legend()
plt.savefig("plots/q2a.png", format = "png", dpi = 350)
plt.close()

#Error
x = np.linspace(start = 0.8, stop = 0.86, num = 200)
plt.plot(x, np.abs(numpyLagrange(x, xList1, yList1) - np.exp(x)), 'k--', label = r"$l_1(x)$")
plt.plot(x, np.abs(numpyLagrange(x, xList2, yList2) - np.exp(x)), 'k', label = r"$l_2(x)$")
plt.xlabel(r"x")
plt.ylabel(r"error")
plt.grid(True)
plt.yscale("log")
plt.legend()
plt.savefig("plots/q2b.png", format = "png", dpi = 350)
plt.close()
