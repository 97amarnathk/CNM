import numpy as np
import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pylab as plt
plt.ion()


def NDD(data, x):
    #Number of data points
    pts=len(data)

    #Number of x points
    nx = len(x)

    #Parse x, y data points
    X = [d[0] for d in data]
    Y = [d[1] for d in data]

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

if '__main__' in __name__:
    x = lambda n: np.linspace(-1,1,n)
    f = lambda x: np.cos(np.sin(np.pi*x))

    p=5
    data=zip(x(p),f(x(p)))
    X = [d[0] for d in data]
    Y = [d[1] for d in data]
    x0=X[0];x1=X[1];x2=X[2];x3=X[3];x4=X[4]

    NX=x(200)
    NY = NDD(data, NX)

    plt.plot(NX,NY,'r')
    plt.plot(x(200),f(x(200)),'k')
