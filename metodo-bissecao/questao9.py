import numpy as np

def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

def bisseccao(f,a,b,tol=1e-5):

    while (b-a)/2 > tol:

        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


raiz = bisseccao(f,0.5,1.5)

print("Raiz:",raiz)