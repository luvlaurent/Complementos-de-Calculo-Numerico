# g(x) = 2^-x

import math

def g(x):
    return 2**(-x)

p = 0.5
tol = 1e-4
erro = 1
iteracao = 0

while erro > tol:
    p_new = g(p)
    erro = abs(p_new - p)

    p = p_new
    iteracao += 1

print(f"Ponto fixo: {p:.6f}")
print(f"Iterações: {iteracao}")
