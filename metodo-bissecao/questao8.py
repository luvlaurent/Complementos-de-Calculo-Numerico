import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - np.tan(x)

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

# bissecção
raiz, it = bisseccao(f, 4, 5, 1e-5, 100)

print("Raiz:", raiz)
print("Iterações:", it)

# gráfico
x = np.linspace(-6,6,1000)
plt.plot(x, x, label="y = x")
plt.plot(x, np.tan(x), label="y = tan(x)")
plt.ylim(-10,10)
plt.legend()
plt.grid()
plt.show()
