# QUESTÃO 11
# Aproximação de sqrt(3)

import math

def g(x):
    return 0.5 * (x + 3/x)

p = 1
tol = 1e-4

for i in range(100):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"sqrt(3) ≈ {p_new:.6f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
