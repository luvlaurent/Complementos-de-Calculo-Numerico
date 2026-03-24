# QUESTÃO 12
# Aproximação de raiz cúbica de 25

import math

def g(x):
    return (2*x + 25/(x**2))/3

p = 1
tol = 1e-4

for i in range(100):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"Raiz cúbica de 25 ≈ {p_new:.6f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
