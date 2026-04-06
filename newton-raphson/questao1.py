import math
# --------------------------------------------------
# QUESTÃO 1
# f(x) = x^2 - 6
# p0 = 1
# Calcular p2 usando Newton
# --------------------------------------------------
# Lista 3 - QUESTÃO 1 - Método de Newton

# função f(x)
def f(x):
    return x**2 - 6

# derivada f'(x)
def df(x):
    return 2*x

# valor inicial
p = 1

print("Iteração | Valor de p")

# vamos calcular até p2
for i in range(2):
    p = p - f(p)/df(p)
    print(i+1, "      |", p)
