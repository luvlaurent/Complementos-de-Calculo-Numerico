import math

# --------------------------------------------------
# QUESTÃO 2
# x0 = 1, x1 = 1.25, x2 = 1.6
# Aproximar f(1.4)
# --------------------------------------------------

x = [1,1.25,1.6]
xp = 1.4

funcoes = {
    "a) sin(pi x)": lambda x: math.sin(math.pi*x),
    "b) raiz cubica(x-1)": lambda x: (x-1)**(1/3),
    "c) log10(3x-1)": lambda x: math.log10(3*x-1),
    "d) e^(2x)-x": lambda x: math.exp(2*x)-x
}

def lagrange(xi, yi, x):
    soma = 0
    for i in range(len(xi)):
        termo = yi[i]
        for j in range(len(xi)):
            if i != j:
                termo *= (x-xi[j])/(xi[i]-xi[j])
        soma += termo
    return soma


for nome,f in funcoes.items():
    
    print("\n",nome)
    
    y = [f(xi) for xi in x]
    
    p1 = lagrange(x[:2],y[:2],xp)
    p2 = lagrange(x,y,xp)
    
    real = f(xp)
    
    print("Grau1:",p1,"Erro:",abs(real-p1))
    print("Grau2:",p2,"Erro:",abs(real-p2))