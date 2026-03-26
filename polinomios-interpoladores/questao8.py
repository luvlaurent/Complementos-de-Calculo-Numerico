# Questão 8 

import numpy as np

def f(x):
    return np.exp(x)

def lagrange(x_pontos, y_pontos, x):
    n = len(x_pontos)
    i = 0
    resultado = 0

    while i < n:
        termo = y_pontos[i]
        j = 0
        while j < n:
            if i != j:
                termo = termo * (x - x_pontos[j]) / (x_pontos[i] - x_pontos[j])
            j += 1
        resultado += termo
        i += 1

    return resultado

x_pontos = [0, 0.25, 0.5]
y_pontos = [f(x_pontos[0]), f(x_pontos[1]), f(x_pontos[2])]

x = 0.43

p1 = lagrange(x_pontos[:2], y_pontos[:2], x)
p2 = lagrange(x_pontos, y_pontos, x)

real = f(x)

print("P1:", p1)
print("P2:", p2)
print("Erro P1:", abs(real - p1))
print("Erro P2:", abs(real - p2))
