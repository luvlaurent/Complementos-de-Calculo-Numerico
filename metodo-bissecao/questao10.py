import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 1 - np.exp(1 - x**2)

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

raiz, it = bisseccao(f, -2, 0, 1e-3, 100)

print("Raiz:", raiz)

# gráfico
x = np.linspace(-2,2,1000)
y1 = x**2 - 1
y2 = np.exp(1 - x**2)

plt.plot(x, y1, label="y = x^2 - 1")
plt.plot(x, y2, label="y = e^(1-x^2)")
plt.legend()
plt.grid()
plt.show()
