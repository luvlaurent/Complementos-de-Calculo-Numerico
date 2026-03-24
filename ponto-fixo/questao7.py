# Resolver x^4 - 3x^2 - 3 = 0

import math

def g(x):
    return math.sqrt((x**4 - 3)/3)

p = 1
tol = 1e-2
erro = 1
iteracao = 0

while erro > tol:
    p_new = g(p)
    erro = abs(p_new - p)

    p = p_new
    iteracao += 1

print(f"Solução aproximada: {p:.4f}")
print(f"Iterações: {iteracao}")
