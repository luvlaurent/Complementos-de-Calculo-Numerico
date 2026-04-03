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


# ===============================
# ITEM (a)
# ===============================

x1 = np.array([8.1, 8.3, 8.6, 8.7])
y1 = np.array([16.94410, 17.56492, 18.50515, 18.82091])

tabela1 = diferencas_divididas(x1, y1)

x_aprox = 8.4

p1 = newton(x1[:2], tabela1[:2,:2], x_aprox)
p2 = newton(x1[:3], tabela1[:3,:3], x_aprox)
p3 = newton(x1, tabela1, x_aprox)

print("Questão 1(a):")
print("Grau 1:", p1)
print("Grau 2:", p2)
print("Grau 3:", p3)

# ===============================
# ITEM (b)
# ===============================

x2 = np.array([0.6, 0.7, 0.8, 1.0])
y2 = np.array([-0.17694460, 0.01375227, 0.22363362, 0.65809197])

tabela2 = diferencas_divididas(x2, y2)

x_aprox = 0.9

p1 = newton(x2[:2], tabela2[:2,:2], x_aprox)
p2 = newton(x2[:3], tabela2[:3,:3], x_aprox)
p3 = newton(x2, tabela2, x_aprox)

print("\nQuestão 1(b):")
print("Grau 1:", p1)
print("Grau 2:", p2)
print("Grau 3:", p3)

# ===============================
# GRÁFICO (exemplo item a)
# ===============================

xx = np.linspace(8.1, 8.7, 100)
yy = [newton(x1, tabela1, xi) for xi in xx]

plt.plot(xx, yy)
plt.scatter(x1, y1)
plt.title("Interpolação - Questão 1(a)")
plt.show()