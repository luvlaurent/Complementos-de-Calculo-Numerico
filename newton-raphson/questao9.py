# QUESTÃO 9
# g(x) = x + 0.5*sin(x/2)

import math

def g(x):
    return x + 0.5 * math.sin(x/2)

p = 1
tol = 1e-2

for i in range(200):
    p_new = g(p)
    if abs(p_new - p) < tol:
        print(f"Ponto fixo: {p_new:.4f}")
        print(f"Iterações: {i+1}")
        break
    p = p_new
