# Questão 11
import numpy as np

def f(x):
    return (x+2)*(x+1)*x*(x-1)**3*(x-2)

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
    print("QUESTÃO 11")

    print("\n(a)", bisseccao(f, -3, 1))
    print("(b)", bisseccao(f, -2.5, 3))
    print("(c)", bisseccao(f, -1.75, 1.5))
    print("(d)", bisseccao(f, -1.5, 1.75))

if __name__ == "__main__":
    main()
