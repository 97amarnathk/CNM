import numpy as np
import matplotlib.pyplot as plt

def bisectionRoot(f, a, b, e):
    rootList = []
    a = round(a, 5)
    b = round(b, 5)
    rootList.append(b)
    c = (a + b)/2.0
    rootList.append(c)
    if f(a) * f(b) > 0:
        return "Error"
    while np.abs(a-b) >= e:
        c = round((a + b)/2, 5)
        fa = f(a)
        fc = f(c)
        rootList.append(c)
        if fa * fc > 0:
            a = c
        else:
            b=c
    return rootList

def newtonRalphsonRoot(f, dfdx, a):
     rootList = []
     a = round(a,5)
     rootList.append(a)
     if dfdx(a)==0:
        return "Error"
     an = round(a - f(a)/dfdx(a), 5)
     rootList.append(an)
     while an - a != 0:
         a = an
         if dfdx(a)==0:
             return "Error"
         an = round(a - f(a)/dfdx(a), 5)
         rootList.append(an)
     return rootList

funcList = []
derivativeList = []
guess = []

#q1
funcList.append(lambda x: x**6 - x - 1)
derivativeList.append(lambda x: 6*(x**5) - 1)
guess.append([1, 2])

#q2
funcList.append(lambda x: x**3 - x**2 - x- 1)                                                   
derivativeList.append(lambda x: 3*(x**2)- 2*x - 1)
guess.append([1, 2])

#q3
funcList.append(lambda x: x - 1 - 0.3*np.cos(x))
derivativeList.append(lambda x:1 + 0.3*np.sin(x))
guess.append([0, np.pi/2])

#q4
funcList.append(lambda x: 0.5 + np.sin(x) - np.cos(x))
derivativeList.append(lambda x: np.cos(x) + np.sin(x))
guess.append([0, np.pi/4])

#q5
funcList.append(lambda x: x - np.exp(-x))
derivativeList.append(lambda x: 1 + np.exp(-x))
guess.append([0, 1])

#q6
funcList.append(lambda x: np.sin(x) - np.exp(-x))
derivativeList.append(lambda x: np.cos(x) + np.exp(x))
guess.append([0, np.pi/2])

#q7
funcList.append(lambda x: x**3 - 2*x - 2)
derivativeList.append(lambda x: 3*x**2 - 2)
guess.append([1, 2])

#q8
funcList.append(lambda x: x**4 - x - 1)
derivativeList.append(lambda x: 4*x**3 - 1)
guess.append([1, 2])

#q9
funcList.append(lambda x: x**4 - x - 1)                                                   
derivativeList.append(lambda x: 4*x**3 - 1)                                               
guess.append([-1, 0])

#q10
funcList.append(lambda x: np.exp(x) - x - 2)
derivativeList.append(lambda x: np.exp(x) - 1)
guess.append([1, 2])

#q11
funcList.append(lambda x: np.sin(x) + 1 - x)
derivativeList.append(lambda x: np.cos(x) - 1)
guess.append([np.pi/2, np.pi])

count = 1
for f, d, g in zip(funcList, derivativeList, guess):
    rootsBisection =  np.array(bisectionRoot(f, g[0], g[1], 0.0001))
    rootsNR = np.array(newtonRalphsonRoot(f, d, g[1]))
    plt.plot(np.arange(1, len(rootsBisection) + 1), np.abs(f(rootsBisection)), 'ko-', markersize = 4, label = "Bisection")
    plt.plot(np.arange(1, len(rootsNR) + 1), np.abs(f(rootsNR)), 'k^:', markersize = 4, label = "Newton Ralphson")
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.savefig("root"+str(count)+".png", format = "png", dpi = 350)
    plt.close()
    count= count+1
