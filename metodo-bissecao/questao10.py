# Questão 10
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 1 - np.exp(1 - x**2)

def bisseccao(f, a, b, tol=1e-3, max_iter=100):
    if f(a)*f(b) >= 0:
        raise ValueError("Intervalo inválido!")

    for i in range(max_iter):
        c = (a + b)/2

        if abs(f(c)) < tol or (b - a)/2 < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c, i+1

def main():
    print("=== QUESTÃO 10 ===")

    # (a)
    print("\n(a) Gráfico:")
    x = np.linspace(-2,2,1000)
    plt.plot(x, x**2 - 1, label="y = x^2 - 1")
    plt.plot(x, np.exp(1 - x**2), label="y = e^(1-x^2)")
    plt.legend()
    plt.grid()
    plt.title("Questão 10 (a)")
    plt.show()

    # (b)
    print("\n(b) Bissecção:")
    raiz, it = bisseccao(f, -2, 0)
    print("Raiz:", raiz)

if __name__ == "__main__":
    main()
