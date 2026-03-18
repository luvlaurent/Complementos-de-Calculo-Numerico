import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 2
# f(x) = 3(x+1)(x-1/2)(x-1)
# Utilizar bisseção para obter p3 nos intervalos:
# a) [-2,1.5]
# b) [-1.25,2.5]
# --------------------------------------------------

def f(x):
    return 3*(x+1)*(x-0.5)*(x-1)

def bissecao_iteracoes(f,a,b,n):
    
    for i in range(n):
        p = (a+b)/2
        
        print("Iteração",i+1,"p =",p)
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return p


# ---------------- Letra A ----------------
print("Letra A:")
raiz_a = bissecao_iteracoes(f,-2,1.5,3)

# ---------------- Letra B ----------------
print("\nLetra B:")
raiz_b = bissecao_iteracoes(f,-1.25,2.5,3)


# ---------------- GRÁFICO ----------------

x = np.linspace(-3,3,400)
y = f(x)

plt.plot(x,y)
plt.axhline(0)
plt.scatter([raiz_a,raiz_b],[0,0])

plt.title("Questão 2")
plt.grid()

plt.show()