# Função
def f(x):
    return x**3 - 7*x**2 + 14*x - 6

# Método da bisseção
def bissecao(f,a,b,tol=1e-2):

    while (b-a)/2 > tol:

        p = (a+b)/2

        if f(a)*f(p) < 0:
            b = p
        else:
            a = p

    return (a+b)/2


# ---------------------
# Letra A
# ---------------------

print("A)",bissecao(f,0,1))


# ---------------------
# Letra B
# ---------------------

print("B)",bissecao(f,1,3.2))


# ---------------------
# Letra C
# ---------------------

print("C)",bissecao(f,3.2,4))