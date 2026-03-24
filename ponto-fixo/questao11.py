# Aproximação de sqrt(3)

import math

def g(x):
    return 0.5 * (x + 3/x)

p = 1
tol = 1e-4
erro = 1
iteracao = 0

while erro > tol:
    p_new = g(p)
    erro = abs(p_new - p)

    p = p_new
    iteracao += 1

print(f"sqrt(3) ≈ {p:.6f}")
print(f"Iterações: {iteracao}")
