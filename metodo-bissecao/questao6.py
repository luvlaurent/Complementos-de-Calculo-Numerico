import math

# Método da bisseção
def bissecao(f,a,b,tol=1e-5):

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

fa = lambda x: 3*x - math.exp(x)

print("A)",bissecao(fa,1,2))


# ---------------------
# Letra B
# ---------------------

fb = lambda x: 2*x + 3*math.cos(x) - math.exp(x)

print("B)",bissecao(fb,0,1))


# ---------------------
# Letra C
# ---------------------

fc = lambda x: x**2 - 4*x + 4 - math.log(x)

print("C) intervalo [1,2]:",bissecao(fc,1,2))
print("C) intervalo [2,4]:",bissecao(fc,2,4))


# ---------------------
# Letra D
# ---------------------

fd = lambda x: x + 1 - 2*math.sin(math.pi*x)

print("D) intervalo [0,0.5]:",bissecao(fd,0,0.5))
print("D) intervalo [0.5,1]:",bissecao(fd,0.5,1))