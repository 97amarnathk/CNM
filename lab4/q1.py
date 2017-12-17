from integration import trapezoidal, simpson
import numpy as np
import matplotlib.pyplot as plt

e = np.e
pi = np.pi

f1 = lambda x: np.exp(x)*np.cos(4*x)
if1 = (np.exp(pi)-1)/17.0

f2 = lambda x: x**(2.5)
if2 = 2/7.0

f3 = lambda x: 1/(1+(x-pi)**2)
if3 = np.arctan(pi) + np.arctan(5-pi)

nList = []
tList = []
sList = []
tErrorList = []
sErrorList = []

for i in range(1, 10):
    n = 2.0**i
    t = trapezoidal(f1, 0, pi, n)
    s = simpson(f1, 0, pi, n)
    nList.append(n)
    tList.append(t)
    sList.append(s)
    tErrorList.append(np.abs(if1 - t))
    sErrorList.append(np.abs(if1 - s))

for i in range(0, 9):
    print int(nList[i]), "&", tList[i], "&", sList[i], "&", tErrorList[i], "&", sErrorList[i], "\\\\"

plt.plot(nList, tList, 'k--', label = r"trapezoidal")
plt.plot(nList, sList, 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Value of integration")
plt.xscale('log', basex = 2)
plt.grid(True)
plt.legend()
plt.savefig("plots/q1a.png", format = "png", dpi = 350)
plt.close()

plt.plot(nList, np.abs(tErrorList), 'k--', label = r"trapezoidal")
plt.plot(nList, np.abs(sErrorList), 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Error")
plt.xscale('log', basex = 2)
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.savefig("plots/q1b.png", format = "png", dpi = 350)
plt.close()

print " "

nList = []
tList = []
sList = []
tErrorList = []
sErrorList = []

for i in range(1, 10):
    n = 2.0**i
    t = trapezoidal(f2, 0, 1, n)
    s = simpson(f2, 0, 1, n)
    nList.append(n)
    tList.append(t)
    sList.append(s)
    tErrorList.append(np.abs(if2 - t))
    sErrorList.append(np.abs(if2 - s))

for i in range(0, 9):
    print int(nList[i]), "&", tList[i], "&", sList[i], "&", tErrorList[i], "&", sErrorList[i], "\\\\"

plt.plot(nList, tList, 'k--', label = r"trapezoidal")
plt.plot(nList, sList, 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Value of integration")
plt.xscale('log', basex = 2)
plt.grid(True)
plt.legend()
plt.savefig("plots/q1c.png", format = "png", dpi = 350)
plt.close()

plt.plot(nList, np.abs(tErrorList), 'k--', label = r"trapezoidal")
plt.plot(nList, np.abs(sErrorList), 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Error")
plt.xscale('log', basex = 2)
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.savefig("plots/q1d.png", format = "png", dpi = 350)
plt.close()

print " "

nList = []
tList = []
sList = []
tErrorList = []
sErrorList = []

for i in range(1, 10):
    n = 2.0**i
    t = trapezoidal(f3, 0, 5, n)
    s = simpson(f3, 0, 5, n)
    nList.append(n)
    tList.append(t)
    sList.append(s)
    tErrorList.append(np.abs(if3 - t))
    sErrorList.append(np.abs(if3 - s))

for i in range(0, 9):
    print int(nList[i]), "&", tList[i], "&", sList[i], "&", tErrorList[i], "&", sErrorList[i], "\\\\"

plt.plot(nList, tList, 'k--', label = r"trapezoidal")
plt.plot(nList, sList, 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Value of integration")
plt.xscale('log', basex = 2)
plt.grid(True)
plt.legend()
plt.savefig("plots/q1e.png", format = "png", dpi = 350)
plt.close()

plt.plot(nList, np.abs(tErrorList), 'k--', label = r"trapezoidal")
plt.plot(nList, np.abs(sErrorList), 'k', label = r"simpson")
plt.xlabel(r"$n$")
plt.ylabel(r"Error")
plt.xscale('log', basex = 2)
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.savefig("plots/q1f.png", format = "png", dpi = 350)
plt.close()
