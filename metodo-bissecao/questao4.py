# Função
def f(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

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

print("A)",bissecao(f,-2,-1))


# ---------------------
# Letra B
# ---------------------

print("B)",bissecao(f,0,2))


# ---------------------
# Letra C
# ---------------------

print("C)",bissecao(f,2,3))


# ---------------------
# Letra D
# ---------------------

print("D)",bissecao(f,-1,0))