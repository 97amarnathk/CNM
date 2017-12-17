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

xList = [0.0, 1.0, 2.0]
yList = [-1.0, -1.0, 7.0]

x = np.linspace(start = -1, stop = 3, num = 200)

#plot the point marks
plt.plot(xList, yList, 'ko')
#plot lagrange interpolation
plt.plot(x, numpyLagrange(x, xList, yList), 'k')
plt.xlabel(r"x")
plt.ylabel(r"y")
plt.grid(True)
plt.savefig("plots/q3a.png", format = "png", dpi = 350)
plt.close()

#plot the point marks
plt.plot(xList, yList, 'ko')
#plot lagrange interpolation
plt.plot(x, NDD(x, xList, yList), 'k')
plt.xlabel(r"x")
plt.ylabel(r"y")
plt.grid(True)
plt.savefig("plots/q3b.png", format = "png", dpi = 350)
plt.close()
