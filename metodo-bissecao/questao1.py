import math

# Função
def f(x):
    return math.sqrt(x) - math.cos(x)

# Método da bisseção
def bissecao(f,a,b,tol=1e-6,max_iter=100):

    if f(a)*f(b) > 0:
        print("Não há raiz no intervalo")
        return None

    for i in range(max_iter):

        p = (a+b)/2

        if abs(f(p)) < tol or (b-a)/2 < tol:
            return p

        if f(a)*f(p) < 0:
            b = p
        else:
            a = p

    return p


# Resultado
raiz = bissecao(f,0,1)

print("Raiz aproximada:",raiz)