
# QUESTÃO 2

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

xs = [1, 1.25, 1.6]
x = 1.4

# pontos mais próximos
xs_g1 = [1.25, 1.6]

print("\n=== QUESTÃO 2 ===")

# (a)
f = lambda x: math.sin(math.pi*x)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(a) sin(pi*x)")
print("G1:", lagrange(x, xs_g1, [ys[1], ys[2]]))
print("G2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[1], ys[2]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (b)
f = lambda x: (x-1)**(1/3)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(b) raiz cubica")
print("G1:", lagrange(x, xs_g1, [ys[1], ys[2]]))
print("G2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[1], ys[2]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (c)
f = lambda x: math.log10(3*x - 1)
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(c) log10")
print("G1:", lagrange(x, xs_g1, [ys[1], ys[2]]))
print("G2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[1], ys[2]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))

# (d)
f = lambda x: math.exp(2*x) - x
ys = [f(xi) for xi in xs]
real = f(x)

print("\n(d) exp")
print("G1:", lagrange(x, xs_g1, [ys[1], ys[2]]))
print("G2:", lagrange(x, xs, ys))
print("Erro G1:", erro(real, lagrange(x, xs_g1, [ys[1], ys[2]])))
print("Erro G2:", erro(real, lagrange(x, xs, ys)))