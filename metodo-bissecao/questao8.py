import numpy as np
import matplotlib.pyplot as plt

# função da equação
def f(x):
    return x - np.tan(x)

# método da bissecção
def bisseccao(f, a, b, tol=1e-5):

    if f(a)*f(b) >= 0:
        print("Intervalo inválido")
        return None

    while (b - a)/2 > tol:

        c = (a + b)/2

        if f(c) == 0:
            return c

        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a + b)/2

# intervalo
raiz = bisseccao(f,4,5)

print("Raiz aproximada:",raiz)


# gráfico
x = np.linspace(-6,6,1000)

plt.plot(x,x,label="y=x")
plt.plot(x,np.tan(x),label="y=tan(x)")
plt.ylim(-10,10)

plt.legend()
plt.grid()
plt.show()