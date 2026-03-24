# QUESTÃO 4

import math

print("\nQUESTÃO 4 ")

x = 1.4
xs = [1, 1.25, 1.6]

produto = abs((x-xs[0])*(x-xs[1])*(x-xs[2]))

# exemplo: e^(2x) → derivada terceira ≈ 8e^(2x)
M = 8 * math.exp(2*1.6)

erro_max = (M/math.factorial(3)) * produto

print("Limitante do erro:", erro_max)