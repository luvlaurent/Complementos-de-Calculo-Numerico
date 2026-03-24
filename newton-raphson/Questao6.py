# QUESTÃO 6
# Comparação de métodos para calcular 7^(1/5)

import math

# valor real
real = 7**(1/5)

# número de iterações
n_iter = 10

# métodos
def metodo_a(p):
    return p * (1 + (7 - p**5)/(p**2))**3

def metodo_b(p):
    return p - (p**5 - 7)/(p**2)

def metodo_c(p):
    return p - (p**5 - 7)/(5*p**4)

def metodo_d(p):
    return p - (p**5 - 7)/12

metodos = [metodo_a, metodo_b, metodo_c, metodo_d]

# execução
for i, metodo in enumerate(metodos):
    p = 1
    print(f"\nMétodo {chr(97+i)}:")
    for k in range(n_iter):
        p = metodo(p)
        erro = abs(p - real)
        print(f"Iter {k+1}: p = {p:.6f}, erro = {erro:.6f}")
