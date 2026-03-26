# Questão 9

import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')

pontos = [(0,0), (0.5,y), (1,3), (2,2)]

P = 0
i = 0

while i < 4:
    xi, yi = pontos[i]
    termo = yi
    j = 0
    while j < 4:
        if i != j:
            xj, _ = pontos[j]
            termo *= (x - xj)/(xi - xj)
        j += 1
    P += termo
    i += 1

coef = sp.expand(P).coeff(x,2)

sol = sp.solve(coef - 6, y)

print("y =", sol)
