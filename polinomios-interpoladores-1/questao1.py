import math

# --------------------------------------------------
# QUESTÃO 1
# x0 = 0, x1 = 0.6, x2 = 0.9
# Aproximar f(0.45) com:
# - polinômio de grau 1
# - polinômio de grau 2
# Calcular erro absoluto
# --------------------------------------------------

x = [0, 0.6, 0.9]
xp = 0.45  # ponto de interesse

# Funções
funcoes = {
    "a) cos(x)": math.cos,
    "b) sqrt(1+x)": lambda x: math.sqrt(1+x),
    "c) ln(1+x)": lambda x: math.log(1+x),
    "d) tan(x)": math.tan
}

# Lagrange geral
def lagrange(xi, yi, x):
    n = len(xi)
    soma = 0
    
    for i in range(n):
        termo = yi[i]
        for j in range(n):
            if i != j:
                termo *= (x - xi[j])/(xi[i] - xi[j])
        soma += termo
    
    return soma


for nome,f in funcoes.items():
    
    print("\n",nome)
    
    y = [f(xi) for xi in x]
    
    # Grau 1 (usa x0 e x1)
    p1 = lagrange(x[:2], y[:2], xp)
    
    # Grau 2 (usa todos)
    p2 = lagrange(x, y, xp)
    
    real = f(xp)
    
    print("Grau 1:",p1,"Erro:",abs(real-p1))
    print("Grau 2:",p2,"Erro:",abs(real-p2))