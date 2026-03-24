
# QUESTÃO 3

import math

print("\n=== QUESTÃO 3 ===")

x = 0.45
xs = [0, 0.6, 0.9]

# produto do erro
produto = abs((x-xs[0])*(x-xs[1])*(x-xs[2]))

# exemplo: cos(x) → M = 1
M = 1

erro_max = (M/math.factorial(3)) * produto

print("Limitante do erro:", erro_max)