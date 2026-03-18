# a) Esboce os gráficos de y = e^x − 2 e y = cos(e^x − 2)
# b) Utilize o método da bissecção para determinar uma aproximação com precisão de
# 10^-5 no intervalo [0.5 , 1.5]

import numpy as np
import matplotlib.pyplot as plt


# função para aplicar o método da bissecção
# f(x) = e^x − 2 − cos(e^x − 2)
def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)


# método da bissecção com contagem de iterações
def bisseccao(f, a, b, tol=1e-5, N=20):

    iteracoes = 0

    while iteracoes <= N:
        if (b - a)/2 > tol:c = (a + b)/2
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracoes += 1
    raiz = (a + b)/2
    return raiz, iteracoes
    


# intervalo dado no problema
raiz, n_iter = bisseccao(f, 0.5, 1.5)

print("Raiz aproximada:", raiz)
print("Número de iterações:", n_iter)


# --------- PARTE (a): GRÁFICO ---------

x = np.linspace(0.5, 1.5, 400)

y1 = np.exp(x) - 2
y2 = np.cos(np.exp(x) - 2)

plt.plot(x, y1, label="y = e^x - 2")
plt.plot(x, y2, label="y = cos(e^x - 2)")

# marca a solução encontrada
plt.scatter(raiz, np.exp(raiz)-2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Interseção das funções")
plt.legend()
plt.grid()

plt.show()