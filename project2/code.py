import numpy as np
import matplotlib.pyplot as plt
import math

G = 6.674*(10**(-11))
M = 2.0 * (10**(30))
cinf = 10000
pinf = 10**(-21)
n = 2.5
pi = math.pi

gamma = 1.0/n + 1

mdot = pi*G*G*M*M*(pinf/(cinf*cinf*cinf))*(((2)/(5-3*gamma))**((5-3*gamma)/(2*gamma - 2)))

udot = (mdot/(4*pi*pinf))*(cinf**(2*n))

rinit = 1.0 + math.log(4, 10)
rend = 3.0 + math.log(4, 10)
rStep = 0.01
rScale = 7 * (10**8)

eps = 0.0001

def p(v, r):
    ans = mdot/(4*pi*v*r*r)
    return ans

def c(v , r):
    ans = cinf*((p(v, r)/pinf)**((gamma-1)/2))
    return ans

def f(v, r):
    a1 = (v**2)/2
    a2 = n*((udot/(v*r*r))**(1/n))
    a3 = -1*G*M/r
    a4 = -1*n*(cinf**2)
    ans = a1 + a2 + a3 + a4
    return ans

def bisectionRoot(r, a, b, eps):
    while abs(a-b)>eps:
        c = (a+b)/2
        if f(a, r) * f(c, r) <0:
            b=c
        else:
            a=c
    return (a+b)/2

#Find Vs for a given r
def findV(r_in):
    vmin = 0.0001
    vmax = 1.0 * 10**5
    vstep = 0.1

    r = (10.0**r_in)*rScale
    v = vmin
    l1, r1, l2, r2 = -1, -1, -1, -1

    while v<vmax and v+vstep<vmax:
        if f(v, r)*f(vstep+v, r)<0:
            l1, r1 = v, v+vstep
            print "found V:", v, v+vstep
            break
        v+=vstep

    v+=vstep

    while v<vmax and v+vstep<vmax:
        if f(v, r)*f(vstep+v, r)<0:
            l2, r2 = v, v+vstep
            print "found V:", v, v+vstep
            break
        v+=vstep

    root1 = bisectionRoot(r, l1, r1, eps)
    root2 = bisectionRoot(r, l2, r2, eps)
    return root1, root2

rList = np.linspace(start = rinit, stop = rend, num = math.ceil((rend-rinit)/rStep))
root1List = []
root2List = []

for r in rList:
    print "r", r
    root1, root2 = findV(r)
    root1 = root1/c(root1, (10.0**r)*rScale)
    root2 = root2/c(root2, (10.0**r)*rScale)
    root1List.append(root1)
    root2List.append(root2)

plt.plot(rList, root1List, "k")
plt.plot(rList, root2List, "k--")
plt.show()
