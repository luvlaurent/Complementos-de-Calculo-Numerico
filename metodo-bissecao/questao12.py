# Questão 12
import numpy as np

def f(x):
    return (x+2)*(x+1)**2*x*(x-1)**3*(x-2)

def bisseccao(f, a, b, tol=1e-5, max_iter=100):
    if f(a)*f(b) >= 0:
        return "Sem mudança de sinal"

    for i in range(max_iter):
        c = (a + b)/2

        if abs(f(c)) < tol or (b - a)/2 < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c

def main():
    print("=== QUESTÃO 12 ===")

    print("\n(a)", bisseccao(f, -1.5, 2.5))
    print("(b)", bisseccao(f, -0.5, 2.4))
    print("(c)", bisseccao(f, -0.5, 3))
    print("(d)", bisseccao(f, -3, -0.5))

if __name__ == "__main__":
    main()
