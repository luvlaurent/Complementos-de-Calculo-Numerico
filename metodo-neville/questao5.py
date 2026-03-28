# Questão 5

import numpy as np  # padrão (mesmo não usando muito)

x = 2.5

# polinômios dados
P01 = 2*x + 1
P02 = x + 1
P123 = 3

# cálculo usando ideia do método de Neville
resultado = ((x-3)*P02 - (x-0)*P123)/(0-3)

print("5:", resultado)

# explicação simples:
# combinamos polinômios menores para formar um de grau maior
