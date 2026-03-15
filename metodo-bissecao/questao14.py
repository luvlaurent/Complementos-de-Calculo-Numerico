# QUESTÃO 14
# Aproximação da raiz quadrada de 3 usando bissecção

def f(x):
    return x**2 - 3

def bisseccao(f,a,b,tol=1e-4):

    while (b-a)/2 > tol:

        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2


raiz = bisseccao(f,1,2)

print("Aproximação da raiz de 3:",raiz)