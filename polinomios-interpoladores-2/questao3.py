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

x = np.array([-0.1, 0.0, 0.2, 0.3])
y = np.array([5.3, 2.0, 3.19, 1.0])

tabela = diferencas_divididas(x, y)

valor = 0.15
p = newton(x, tabela, valor)

print("Interpolação grau 3:", p)

# Com novo ponto
x2 = np.append(x, 0.35)
y2 = np.append(y, 0.97260)

tabela2 = diferencas_divididas(x2, y2)

p2 = newton(x2, tabela2, valor)

print("Grau 4:", p2)