# QUESTÃO 12
# Método da bissecção para outra função polinomial

import numpy as np

def f(x):
    return (x+2)*(x+1)**2*x*(x-1)**3*(x-2)

def bisseccao(f, a, b, tol=1e-6):

    if f(a)*f(b) >= 0:
        print("Não há mudança de sinal no intervalo")
        return None

    while (b-a)/2 > tol:

        c = (a+b)/2

        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


# a) [-1.5,2.5]
print("a)", bisseccao(f,-1.5,2.5))

# b) [-0.5,2.4]
print("b)", bisseccao(f,-0.5,2.4))

# c) [-0.5,3]
print("c)", bisseccao(f,-0.5,3))

# d) [-3,-0.5]
print("d)", bisseccao(f,-3,-0.5))