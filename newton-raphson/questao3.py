import math
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 3
# f(x) = x^2 - 6
# p0 = 3, p1 = 2
# calcular p3
# comparar secante e falsa posição
# --------------------------------------------------

def f(x):
    return x**2 - 6


# -------- SECANTE --------
def secante(p0,p1,n_iter):
    
    for i in range(n_iter):
        p = p1 - f(p1)*(p1-p0)/(f(p1)-f(p0))
        print(f"Secante p{i+2} =",p)
        p0,p1 = p1,p
    
    return p


# -------- FALSA POSIÇÃO --------
def falsa_posicao(a,b,n_iter):
    
    for i in range(n_iter):
        p = b - f(b)*(b-a)/(f(b)-f(a))
        print(f"Falsa posição p{i+2} =",p)
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
    
    return p


print("Secante:")
ps = secante(3,2,2)

print("\nFalsa posição:")
pf = falsa_posicao(3,2,2)

# valor real
real = math.sqrt(6)

print("\nValor real:",real)
print("Erro secante:",abs(ps-real))
print("Erro falsa posição:",abs(pf-real))


# -------- GRÁFICO --------
x = np.linspace(0,4,400)
plt.plot(x,f(x))
plt.axhline(0)
plt.scatter([ps,pf],[0,0])

plt.title("Questão 3")
plt.grid()
plt.show()