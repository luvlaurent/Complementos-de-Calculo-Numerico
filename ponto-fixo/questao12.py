# Aproximação da raiz cúbica de 25

import math

def g(x):
    return (2*x + 25/(x**2))/3

p = 1
tol = 1e-4
erro = 1
iteracao = 0

while erro > tol:
    p_new = g(p)
    erro = abs(p_new - p)

    p = p_new
    iteracao += 1

print(f"Raiz cúbica de 25 ≈ {p:.6f}")
print(f"Iterações: {iteracao}")
