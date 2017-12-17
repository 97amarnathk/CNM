import numpy as np

def trapezoidal(f, a, b, n):
    if a==b:
        return 0
    if a>b:
        a,b = b,a
    h = (b-a)/(n*1.0)
    summation = 0
    x = a
    while x<=b:
        summation += f(x)
        x += h
    summation -= (f(a)+f(b))/2.0
    return h*summation

def simpson(f, a, b, n):
    if a==b:
        return 0
    if a>b:
        a,b = b,a
    h = (b-a)/(n*1.0)
    summation = 0
    x = a
    w = 1
    while(x<=b):
        summation += w*f(x)
        if w==1:
            w=4
        elif w==4 and x+h==b:
            w=1
        elif w==4:
            w=2
        elif w==2:
            w=4
        x+=h
    return summation*h/3.0
