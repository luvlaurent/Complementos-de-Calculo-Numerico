import numpy as np
import matplotlib.pyplot as plt
import math

# --------------------------------------------------
# QUESTÃO 7
# a) Esboçar os gráficos de y = x e y = 2 sen(x)
# b) Encontrar solução de x = 2 sen(x) com bisseção
# --------------------------------------------------

# --------- LETRA A (GRÁFICO) ---------

x = np.linspace(0,4,400)

y1 = x
y2 = 2*np.sin(x)

plt.plot(x,y1,label="y = x")
plt.plot(x,y2,label="y = 2sen(x)")

plt.legend()
plt.grid()
plt.title("Questão 7")

plt.show()


# --------- LETRA B (BISSEÇÃO) ---------

def f(x):
    return x - 2*math.sin(x)

def bissecao(f,a,b,tol=1e-5):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


raiz = bissecao(f,1,2)

print("Raiz aproximada:",raiz)