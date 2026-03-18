import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 3
# Resolver x^3 - 7x^2 + 14x - 6 = 0
# com precisão 10^-2 nos intervalos:
# a) [0,1] b) [1,3.2] c) [3.2,4]
# --------------------------------------------------

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

def bissecao(f,a,b,tol=1e-2):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


# --------- Letras ---------

ra = bissecao(f,0,1)
rb = bissecao(f,1,3.2)
rc = bissecao(f,3.2,4)

print("A)",ra)
print("B)",rb)
print("C)",rc)


# --------- GRÁFICO ---------

x = np.linspace(0,4,400)
y = f(x)

plt.plot(x,y)
plt.axhline(0)
plt.scatter([ra,rb,rc],[0,0,0])

plt.title("Questão 3")
plt.grid()
plt.show()