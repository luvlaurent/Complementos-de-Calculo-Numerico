import numpy as np
import matplotlib.pyplot as plt
import math


# ---------------------
# Letra A - Gráfico
# ---------------------

x = np.linspace(0,4,400)

y1 = x
y2 = 2*np.sin(x)

plt.plot(x,y1,label="y = x")
plt.plot(x,y2,label="y = 2 sen(x)")

plt.legend()
plt.grid()

plt.show()


# ---------------------
# Letra B - Método da bisseção
# ---------------------

def f(x):
    return x - 2*math.sin(x)

def bissecao(f,a,b,tol=1e-5):

    while (b-a)/2 > tol:

        p = (a+b)/2

        if f(a)*f(p) < 0:
            b = p
        else:
            a = p

    return (a+b)/2


raiz = bissecao(f,1,2)

print("Primeira solução positiva:",raiz)