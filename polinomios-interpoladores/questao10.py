# Questão 10

import sympy as sp

x, x1 = sp.symbols('x x1')

def f(valor):
    return sp.sqrt(valor - valor**2)

def P2(x_val):
    pontos = [(0, f(0)), (x1, f(x1)), (1, f(1))]
    P = 0

    i = 0
    while i < 3:
        xi, yi = pontos[i]
        termo = yi
        j = 0
        while j < 3:
            if i != j:
                xj, _ = pontos[j]
                termo *= (x_val - xj)/(xi - xj)
            j += 1
        P += termo
        i += 1

    return P

eq = f(0.5) - P2(0.5) + 0.25

sol = sp.solve(eq, x1)

print("x1 =", sol)
