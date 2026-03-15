# Função
def f(x):
    return 3*(x+1)*(x-0.5)*(x-1)

# Método da bisseção com número fixo de iterações
def bissecao_iteracoes(f,a,b,n):

    for i in range(n):

        p = (a+b)/2

        print("Iteração",i+1,"p =",p)

        if f(a)*f(p) < 0:
            b = p
        else:
            a = p

    return p


# ---------------------
# Letra A
# ---------------------

print("Letra A")
bissecao_iteracoes(f,-2,1.5,3)


# ---------------------
# Letra B
# ---------------------

print("\nLetra B")
bissecao_iteracoes(f,-1.25,2.5,3)