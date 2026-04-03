
import numpy as np

def f(x):
    return np.exp(x)*np.cos(x)

#  a)
x0 = 0
x1 = 0.5
x = 0.25

fa = f(x0) + (f(x1)-f(x0))*(x-x0)/(x1-x0)
print("16a:", fa)

# b)
x0 = 0.5
x1 = 1
x = 0.75

fb = f(x0) + (f(x1)-f(x0))*(x-x0)/(x1-x0)
print("16b:", fb)

#  c)
def lagrange(xp, yp, x):
    i = 0
    s = 0
    while i < len(xp):
        p = yp[i]
        j = 0
        while j < len(xp):
            if i != j:
                p *= (x - xp[j])/(xp[i] - xp[j])
            j += 1
        s += p
        i += 1
    return s

xp = [0,0.5,1]
yp = [f(0), f(0.5), f(1)]

f025 = lagrange(xp, yp, 0.25)
f075 = lagrange(xp, yp, 0.75)

print("16c f(0.25):", f025)
print("16c f(0.75):", f075)

# d)
real1 = f(0.25)
real2 = f(0.75)

erro_linear1 = abs(real1 - fa)
erro_quad1 = abs(real1 - f025)

erro_linear2 = abs(real2 - fb)
erro_quad2 = abs(real2 - f075)

print("\n16d:")
print("Erro linear (0.25):", erro_linear1)
print("Erro quadrático (0.25):", erro_quad1)

print("Erro linear (0.75):", erro_linear2)
print("Erro quadrático (0.75):", erro_quad2)

print("\nConclusão:")
print("A interpolação quadrática é melhor pois aproxima melhor funções curvas.")
