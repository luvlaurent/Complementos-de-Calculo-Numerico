# Questão 6 - Neville com dados diferentes
# usamos novamente a ideia do Neville
# juntando polinômios menores para obter o valor final

import numpy as np

x0 = 1.5

P01 = x0 + 1
P12 = 3*x0 - 1
P123 = 4

# interpolação final
P012 = ((x0 - 2)*P01 + (0 - x0)*P12)/(0 - 2)
P0123 = ((x0 - 3)*P012 + (0 - x0)*P123)/(0 - 3)

print(P0123)

