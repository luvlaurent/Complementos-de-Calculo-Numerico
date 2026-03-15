# QUESTÃO 11
# Método da bissecção aplicado em diferentes intervalos

import numpy as np

def f(x):
    return (x+2)*(x+1)*x*(x-1)**3*(x-2)

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


# a) intervalo [-3,1]
print("a)", bisseccao(f,-3,1))

# b) intervalo [-2.5,3]
print("b)", bisseccao(f,-2.5,3))

# c) intervalo [-1.75,1.5]
print("c)", bisseccao(f,-1.75,1.5))

# d) intervalo [-1.5,1.75]
print("d)", bisseccao(f,-1.5,1.75))