# g(x) = x + 0.5*sin(x/2)

import math

def g(x):
    return x + 0.5 * math.sin(x/2)

p = 1
tol = 1e-2
erro = 1
iteracao = 0

while erro > tol:
    p_new = g(p)
    erro = abs(p_new - p)

    p = p_new
    iteracao += 1

print(f"Ponto fixo: {p:.4f}")
print(f"Iterações: {iteracao}")
