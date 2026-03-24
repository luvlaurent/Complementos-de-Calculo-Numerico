# QUESTÃO 7
# Resolver x^4 - 3x^2 - 3 = 0 com precisão 1e-2

import math

def g(x):
    return math.sqrt((x**4 - 3)/3)

p = 1
tol = 1e-2

for i in range(100):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"Solução aproximada: {p_new:.4f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
