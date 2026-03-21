# Questão 14
import numpy as np

def f(x):
    return x**2 - 3

def bisseccao(f, a, b, tol=1e-4, max_iter=100):
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
    print("QUESTÃO 14")

    raiz, it = bisseccao(f, 1, 2)
    print("Raiz de sqrt(3):", raiz)

if __name__ == "__main__":
    main()
