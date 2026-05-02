# Questão 5

import numpy as np  # padrão (mesmo não usando muito)

# Aplicação da fórmula de Neville

# A ideia é construir um polinômio de grau maior a partir de dois menores
# Fórmula geral:
# P[i,j](x) = ((x - x_j)*P[i,j-1](x) - (x - x_i)*P[i+1,j](x)) / (x_i - x_j)
# Aqui estamos combinando:
# P02 e P123 para obter um polinômio de grau maior

x = 2.5

# polinômios dados
P01 = 2*x + 1
P02 = x + 1
P123 = 3

# Queremos encontrar P0123
# P[i,j](x) = ((x - x_j)*P[i,j-1](x) - (x - x_i)*P[i+1,j](x)) / (x_i - x_j)
resultado = ((x-3)*P02 - (x-0)*P123)/(0-3)

print("5:", resultado)

