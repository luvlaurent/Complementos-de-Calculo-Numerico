import math

# Método da bisseção
def bissecao(f,a,b,tol=1e-6):

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

fa = lambda x: x - 2**(-x)

print("A)",bissecao(fa,0,1))


# ---------------------
# Letra B
# ---------------------

fb = lambda x: math.exp(x) - x**2 + 3*x - 2

print("B)",bissecao(fb,0,1))


# ---------------------
# Letra C
# ---------------------

fc = lambda x: 2*x*math.cos(2*x) - (x+1)**2

print("C) intervalo [-3,-2]:",bissecao(fc,-3,-2))
print("C) intervalo [-1,0]:",bissecao(fc,-1,0))


# ---------------------
# Letra D
# ---------------------

fd = lambda x: x*math.cos(x) - 2*x**2 + 3*x - 1

print("D) intervalo [0.2,0.3]:",bissecao(fd,0.2,0.3))
print("D) intervalo [1.2,1.3]:",bissecao(fd,1.2,1.3))