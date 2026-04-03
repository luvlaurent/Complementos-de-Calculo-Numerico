import math

# --------------------------------------------------
# QUESTÃO 7
# Comparar erro real e limitante
# --------------------------------------------------

def f(x):
    return x*math.log(x)

def lagrange(xi, yi, x):
    soma = 0
    for i in range(len(xi)):
        termo = yi[i]
        for j in range(len(xi)):
            if i != j:
                termo *= (x-xi[j])/(xi[i]-xi[j])
        soma += termo
    return soma


# pontos da questão 5 (exemplo)
x = [8.1,8.3,8.6]
y = [16.94410,17.56492,18.50515]

xp = 8.4

aprox = lagrange(x,y,xp)
real = f(xp)

erro_real = abs(real-aprox)

# estimativa (valor genérico de derivada)
M = 10
erro_limite = (M/6)*abs((xp-x[0])*(xp-x[1])*(xp-x[2]))

print("Erro real:",erro_real)
print("Limitante:",erro_limite)