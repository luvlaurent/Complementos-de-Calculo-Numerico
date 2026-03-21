import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

def bisseccao(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b)/2

        if abs(f(c)) < tol or (b - a)/2 < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c, i+1

raiz, it = bisseccao(f, 0.5, 1.5, 1e-5, 100)

print("Raiz:", raiz)

# gráfico
x = np.linspace(0,2,1000)
y1 = np.exp(x) - 2
y2 = np.cos(np.exp(x) - 2)

plt.plot(x, y1, label="y = e^x - 2")
plt.plot(x, y2, label="y = cos(e^x - 2)")
plt.legend()
plt.grid()
plt.show()
