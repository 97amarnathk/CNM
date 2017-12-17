from integration import trapezoidal, simpson
import numpy as np
import matplotlib.pyplot as plt

e = np.e
pi = np.pi

f1 = lambda x: np.exp(-1*(x**2))

f2 = lambda x: np.arctan(1 + x**2)

nList = []
tList = []
sList = []

for i in range(1, 10):
    n = 2.0**i
    t = trapezoidal(f1, 0, 10, n)
    s = simpson(f1, 0, 10, n)
    nList.append(n)
    tList.append(t)
    sList.append(s)

for i in range(0, 9):
    print int(nList[i]), "&", tList[i], "&", sList[i], "\\\\"

plt.plot(nList, tList, 'k--', label = r"trapezoidal")
plt.plot(nList, sList, 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Value of integration")
plt.xscale('log', basex = 2)
plt.grid(True)
plt.legend()
plt.savefig("plots/q2a.png", format = "png", dpi = 350)
plt.close()

print " "

nList = []
tList = []
sList = []

for i in range(1, 10):
    n = 2.0**i
    t = trapezoidal(f2, 0, 2, n)
    s = simpson(f2, 0, 2, n)
    nList.append(n)
    tList.append(t)
    sList.append(s)

for i in range(0, 9):
    print int(nList[i]), "&", tList[i], "&", sList[i], "\\\\"

plt.plot(nList, tList, 'k--', label = r"trapezoidal")
plt.plot(nList, sList, 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Value of integration")
plt.xscale('log', basex = 2)
plt.grid(True)
plt.legend()
plt.savefig("plots/q2b.png", format = "png", dpi = 350)
plt.close()
