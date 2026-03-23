import math
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 1
# f(x) = x^4 + 2x^2 - x - 3
# --------------------------------------------------

def f(x):
    return x**4 + 2*x**2 - x - 3

def g1(x):
    return (3 + x - 2*x**2)**(1/4)

def g2(x):
    return ((x + 3 - x**4)/2)**0.5

def g3(x):
    return ((x + 3)/(x**2 + 2))**0.5

def g4(x):
    return (3*x**4 + 2*x**2 + 3)/(4*x**3 + 4*x - 1)

# ---------------- TESTE ----------------

x = 1.2
print("f(x) =",f(x))
print("g1(x)-x =",g1(x)-x)
print("g2(x)-x =",g2(x)-x)
print("g3(x)-x =",g3(x)-x)
print("g4(x)-x =",g4(x)-x)

# ---------------- GRÁFICO ----------------

x_vals = np.linspace(-2,2,400)
plt.plot(x_vals,f(x_vals))
plt.axhline(0)

plt.title("Questão 1")
plt.grid()
plt.show()