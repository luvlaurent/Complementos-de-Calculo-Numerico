import numpy as np

def f(x):
    return x**2 - 1 - np.exp(1 - x**2)

def bisseccao(f,a,b,tol=1e-3):

    while (b-a)/2 > tol:

        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


raiz = bisseccao(f,-2,0)

print("Raiz:",raiz)