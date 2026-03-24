
# QUESTÃO 1

import math

def lagrange(x, xs, ys):
    resultado = 0
    for i in range(len(xs)):
        termo = ys[i]
        for j in range(len(xs)):
            if i != j:
                termo *= (x - xs[j]) / (xs[i] - xs[j])
        resultado += termo
    return resultado

def erro(real, aprox):
    return abs(real - aprox)

# dados
xs = [0, 0.6, 0.9]
x = 0.45

# pontos mais próximos (grau 1)
xs_g1 = [0, 0.6]

print("\n=== QUESTÃO 1 ===")

# (a) cos(x)
f = lambda x: math.cos(x)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(a) cos(x)")
print("Grau 1:", lagrange(x, xs_g1, [ys[0], ys[1]]))
print("Grau 2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[0], ys[1]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (b) sqrt(1+x)
f = lambda x: math.sqrt(1+x)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(b) sqrt(1+x)")
print("Grau 1:", lagrange(x, xs_g1, [ys[0], ys[1]]))
print("Grau 2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[0], ys[1]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (c) ln(x+1)
f = lambda x: math.log(x+1)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(c) ln(x+1)")
print("Grau 1:", lagrange(x, xs_g1, [ys[0], ys[1]]))
print("Grau 2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[0], ys[1]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (d) tan(x)
f = lambda x: math.tan(x)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(d) tan(x)")
print("Grau 1:", lagrange(x, xs_g1, [ys[0], ys[1]]))
print("Grau 2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[0], ys[1]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))