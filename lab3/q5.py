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

xList = [0.0, 1.0, 2.0, 2.5, 3.0, 3.5, 4.0]
yList = [2.5, 0.5, 0.5, 1.5, 1.5, 1.125, 0]

#piecewise linear interpolation
plt.plot(xList, yList, 'ko-')
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q5a.png", format = "png", dpi = 350)
plt.close()

#piecewise quadratic interpolation lagrange
r1 = np.linspace(start = 0, stop = 2, num = 200)
r2 = np.linspace(start = 2, stop = 3, num = 200)
r3 = np.linspace(start = 3, stop = 4, num = 200)
pql1 = numpyLagrange(r1, xList[0:3], yList[0:3])
pql2 = numpyLagrange(r2, xList[2:5], yList[2:5])
pql3 = numpyLagrange(r3, xList[4:7], yList[4:7])
plt.plot(r1, pql1, 'k')
plt.plot(r2, pql2, 'k')
plt.plot(r3, pql3, 'k')
plt.plot(xList, yList, 'ko')
plt.grid(True)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q5b.png", format = "png", dpi = 350)
plt.close()

#piecewise quadratic interpolation newton
r1 = np.linspace(start = 0, stop = 2, num = 200)
r2 = np.linspace(start = 2, stop = 3, num = 200)
r3 = np.linspace(start = 3, stop = 4, num = 200)
pql1 = NDD(r1, xList[0:3], yList[0:3])
pql2 = NDD(r2, xList[2:5], yList[2:5])
pql3 = NDD(r3, xList[4:7], yList[4:7])
plt.plot(r1, pql1, 'k')
plt.plot(r2, pql2, 'k')
plt.plot(r3, pql3, 'k', label = r"piecewise quadratic")
plt.plot(xList, yList, 'k--', label = r"piecewise linear")
plt.plot(xList, yList, 'ko')
plt.grid(True)
plt.legend()
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig("plots/q5c.png", format = "png", dpi = 350)
plt.close()
