# Questão 3 - Aproximar sqrt(3) com Neville

import numpy as np

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

    return Q[0][n-1]

valor_real = np.sqrt(3)

# -------- a)
print("3a - usando f(x) = 3^x")

def f(x):
    return 3**x

xp = [-2,-1,0,1,2]
yp = [f(xp[0]), f(xp[1]), f(xp[2]), f(xp[3]), f(xp[4])]

# queremos sqrt(3) → 3^(1/2)
aprox_a = neville(xp, yp, 0.5)

print("Aproximação:", aprox_a)
print("Valor real:", valor_real)
print("Erro:", abs(valor_real - aprox_a))
print()

# -------- b)
print("3b - usando f(x) = sqrt(x)")

def f(x):
    return np.sqrt(x)

xp = [0,1,2,4,5]
yp = [f(xp[0]), f(xp[1]), f(xp[2]), f(xp[3]), f(xp[4])]

# queremos sqrt(3) → f(3)
aprox_b = neville(xp, yp, 3)

print("Aproximação:", aprox_b)
print("Valor real:", valor_real)
print("Erro:", abs(valor_real - aprox_b))
print()

# -------- c)
print("3c - comparação")

erro_a = abs(valor_real - aprox_a)
erro_b = abs(valor_real - aprox_b)

if erro_a < erro_b:
    print("Melhor: método (a)")
else:
    print("Melhor: método (b)")

print("A melhor aproximação é a que tem menor erro.")
