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

# Função real (item a)
def f_real(x):
    return np.exp(2*x)

# Dados
x = np.array([0.0, 0.25, 0.5, 0.75])
y = np.array([1, 1.64872, 2.71828, 4.48169])

tabela = diferencas_divididas(x, y)

x_aprox = 0.43

p = newton(x, tabela, x_aprox)
real = f_real(x_aprox)

erro = abs(real - p)

print("Aproximação:", p)
print("Valor real:", real)
print("Erro absoluto:", erro)