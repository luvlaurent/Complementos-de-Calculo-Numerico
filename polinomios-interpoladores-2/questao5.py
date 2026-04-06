import numpy as np
import matplotlib.pyplot as plt


# FUNÇÕES BASE (NEWTON)


def diferencas_divididas(x, y):
    """
    Constrói a tabela de diferenças divididas.
    """
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y  # primeira coluna = f(x)

    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (x[i+j] - x[i])

    return tabela


def newton(x, tabela, valor):
    """
    Avalia o polinômio interpolador de Newton.
    """
    n = len(x)
    resultado = tabela[0][0]
    produto = 1.0

    for i in range(1, n):
        produto *= (valor - x[i-1])
        resultado += tabela[0][i] * produto

    return resultado

x = 0.75

P = 1 \
    + 4*x \
    + 4*x*(x - 0.25) \
    + (16/3)*x*(x - 0.25)*(x - 0.5)

print("f(0.75) =", P)
