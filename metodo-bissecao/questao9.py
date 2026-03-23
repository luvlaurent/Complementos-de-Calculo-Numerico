# Questão 9
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

def bisseccao(f, a, b, tol=1e-5, max_iter=100):
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
    print("=== QUESTÃO 9 ===")

    # (a)
    print("\n(a) Gráfico:")
    x = np.linspace(0,2,1000)
    plt.plot(x, np.exp(x)-2, label="y = e^x - 2")
    plt.plot(x, np.cos(np.exp(x)-2), label="y = cos(e^x - 2)")
    plt.legend()
    plt.grid()
    plt.title("Questão 9 (a)")
    plt.show()

    # (b)
    print("\n(b) Bissecção:")
    raiz, it = bisseccao(f, 0.5, 1.5)
    print("Raiz:", raiz)

if __name__ == "__main__":
    main()
