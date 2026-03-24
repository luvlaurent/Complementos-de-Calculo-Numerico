# QUESTÃO 6
# Comparação de métodos para calcular 7^(1/5)

import math

real = 7**(1/5)
tol = 1e-6
max_iter = 50

def metodo_a(p):
    return p * (1 + (7 - p**5)/(p**2))**3

def metodo_b(p):
    return p - (p**5 - 7)/(p**2)

def metodo_c(p):
    return p - (p**5 - 7)/(5*p**4)

def metodo_d(p):
    return p - (p**5 - 7)/12

metodos = [metodo_a, metodo_b, metodo_c, metodo_d]

i = 0
while i < len(metodos):
    metodo = metodos[i]
    p = 1
    erro = 1
    iteracao = 0

    print(f"\nMétodo {chr(97+i)}:")

    while erro > tol and iteracao < max_iter:
        p_new = metodo(p)
        erro = abs(p_new - p)

        print(f"Iter {iteracao+1}: p = {p_new:.6f}, erro = {erro:.6f}")

        p = p_new
        iteracao += 1

    i += 1
