# QUESTÃO 8
# Resolver x^3 - x - 1 = 0

import math

def g(x):
    return (x + 1)**(1/3)

p = 1
tol = 1e-2

for i in range(100):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"Solução aproximada: {p_new:.4f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
