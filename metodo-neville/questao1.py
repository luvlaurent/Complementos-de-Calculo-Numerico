# Questão 1 - Método de Neville

import numpy as np  # não é obrigatório, mas deixei pra padronizar

# função do método de Neville
def neville(xp, yp, x):
    n = len(xp)
    Q = [[0]*n for _ in range(n)]

    i = 0
    while i < n:
        Q[i][0] = yp[i]
        i += 1

    j = 1
    while j < n:
        i = 0
        while i < n - j:
            Q[i][j] = ((x - xp[i+j])*Q[i][j-1] - (x - xp[i])*Q[i+1][j-1])/(xp[i] - xp[i+j])
            i += 1
        j += 1

    return Q

# função pra mostrar resultados por grau
def resolver(xp, yp, x):
    Q = neville(xp, yp, x)
    print("Grau 1:", Q[0][1])
    print("Grau 2:", Q[0][2])
    print("Grau 3:", Q[0][3])
    print()

# a
print("1a")
resolver([8.1,8.3,8.6,8.7],
         [16.94410,17.56492,18.50515,18.82091],
         8.4)

# b
print("1b")
resolver([-0.75,-0.5,-0.25,0],
         [-0.07181250,-0.02475000,0.33493750,1.10100000],
         -1/3)

# c
print("1c")
resolver([0.1,0.2,0.3,0.4],
         [0.62049958,-0.28398668,0.00660095,0.24842440],
         0.25)

# d
print("1d")
resolver([0.6,0.7,0.8,1.0],
         [-0.17694460,0.01375227,0.22363362,0.65809197],
         0.9)
