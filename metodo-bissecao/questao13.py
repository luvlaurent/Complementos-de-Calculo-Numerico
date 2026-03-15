# QUESTÃO 13
# Aproximação da raiz cúbica de 25 usando bissecção

def f(x):
    return x**3 - 25

def bisseccao(f,a,b,tol=1e-4):

    while (b-a)/2 > tol:

        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


raiz = bisseccao(f,2,3)

print("Aproximação da raiz cúbica de 25:",raiz)