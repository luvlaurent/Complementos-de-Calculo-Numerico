import math
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 1
# Utilize o método da bisseção para determinar p,
# para f(x) = sqrt(x) - cos(x) em [0,1]
# --------------------------------------------------

def f(x):
    return math.sqrt(x) - math.cos(x)

def bissecao(f,a,b,tol=1e-6):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


# Cálculo da raiz
raiz = bissecao(f,0,1)

print("Raiz aproximada:",raiz)


# ---------------- GRÁFICO ----------------

x = np.linspace(0,1,200)
y = np.sqrt(x) - np.cos(x)

plt.plot(x,y,label="f(x)")
plt.axhline(0)
plt.scatter(raiz,0)

plt.legend()
plt.grid()
plt.title("Questão 1")

plt.show()