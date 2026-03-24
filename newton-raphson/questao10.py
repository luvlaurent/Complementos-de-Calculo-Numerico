# QUESTÃO 10
# g(x) = 2^-x

import math

def g(x):
    return 2**(-x)

p = 0.5
tol = 1e-4

for i in range(200):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"Ponto fixo: {p_new:.6f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
