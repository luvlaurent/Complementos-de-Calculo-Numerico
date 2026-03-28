# Questão 6 - Neville com dados diferentes
# usamos novamente a ideia do Neville
# juntando polinômios menores para obter o valor final

import numpy as np

x = 1.5

# dados
# P0,1(x) = x + 1
# P1,2(x) = 3x - 1
# P1,2,3(1.5) = 4

P01 = x + 1
P12 = 3*x - 1
P123 = 4

# construção do polinômio maior

P0123 = ((x - 3)*P01 - (x - 0)*P123) / (0 - 3)

print("6 - resultado:", P0123)
