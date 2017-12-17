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

def NDD(x, xList, yList):
    #Number of data points
    pts=len(xList)

    #Number of x points
    nx = len(x)

    #Parse x, y data points
    X = xList
    Y = yList

    #Allocate space for L(x)
    N = [0.0]*(nx)

    def a(j0,j1=None):
        if j1 is None: j1 = j0; j0 = 0

        if j0 == j1: return Y[j0]

        elif j1 - j0 == 1:
            return (Y[j1] - Y[j0]) / (X[j1] - X[j0])
        else:
            return (a(j0+1,j1) - a(j0,j1-1)) / (X[j1]-X[j0])

    def n(j,x_):
        v = 1.0
        for i in xrange(0,j):
            v *= float(x_-X[i])
        return v

    #Construct N(x)
    for i in xrange(nx):
        for j in xrange(0,pts):
            N[i] += a(j)*n(j,x[i])
    return N

xList = [3.35, 3.4, 3.5, 3.6]
yList = [0.298507, 0.294118, 0.285714, 0.277778]

x = np.linspace(start = 1, stop = 6, num = 2000)

l1 = numpyLagrange(x, xList[:2], yList[:2])
l2 = numpyLagrange(x, xList[:3], yList[:3])
l3 = numpyLagrange(x, xList, yList)

n1 = NDD(x, xList[:2], yList[:2])
n2 = NDD(x, xList[:3], yList[:3])
n3 = NDD(x, xList, yList)

#lagrange
plt.plot(x, 1/x, 'k', linewidth = 2, label = r"$y = \frac{1}{x}$")
plt.plot(x, l1, 'k:', linewidth = 1, label = r"$l_1(x)$")
plt.plot(x, l2, 'k--', linewidth = 1, label = r"$l_2(x)$")
plt.plot(x, l3, 'k', linewidth = 1, label = r"$l_3(x)$")
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.savefig("plots/q4a.png", format = "png", dpi = 350)
plt.close()

#newton divided difference
plt.plot(x, 1/x, 'k', linewidth = 2, label = r"$y = \frac{1}{x}$")
plt.plot(x, n1, 'k:', linewidth = 1, label = r"$n_1(x)$")
plt.plot(x, n2, 'k--', linewidth = 1, label = r"$n_2(x)$")
plt.plot(x, n3, 'k', linewidth = 1, label = r"$n_3(x)$")
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.legend()
plt.savefig("plots/q4b.png", format = "png", dpi = 350)
plt.close()

x = np.linspace(start = 2.5, stop = 4.5, num = 2000)

#lagrange error
plt.plot(x, np.abs(l1 - (1/x)), 'k:', label = r"$l_1(x)$")
plt.plot(x, np.abs(l2 - (1/x)), 'k--', label = r"$l_2(x)$")
plt.plot(x, np.abs(l3 - (1/x)), 'k', label = r"$l_3(x)$")
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.yscale("log")
plt.legend()
plt.savefig("plots/q4c.png", format = "png", dpi = 350)
plt.close()

#newton divided difference error
plt.plot(x, np.abs(n1 - (1/x)), 'k:', label = r"$l_1(x)$")
plt.plot(x, np.abs(n2 - (1/x)), 'k--', label = r"$l_2(x)$")
plt.plot(x, np.abs(n3 - (1/x)), 'k', label = r"$l_3(x)$")
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.yscale("log")
plt.legend()
plt.savefig("plots/q4d.png", format = "png", dpi = 350)
plt.close()
