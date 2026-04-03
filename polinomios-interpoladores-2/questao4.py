import numpy as np
import matplotlib.pyplot as plt

# ===============================
# FUNÇÕES BASE (NEWTON)
# ===============================

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

x = np.array([0.0, 0.1, 0.3, 0.6, 1.0])
y = np.array([-6.0, -5.89483, -5.65014, -5.17788, -4.28172])

tabela = diferencas_divididas(x, y)

print(newton(x, tabela, 0.5))

# Grau 5
x2 = np.append(x, 1.1)
y2 = np.append(y, -3.99583)

tabela2 = diferencas_divididas(x2, y2)

print(newton(x2, tabela2, 0.5))