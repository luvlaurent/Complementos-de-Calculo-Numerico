import math
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 5
# Comparar convergência
# --------------------------------------------------

valor_real = 21**(1/3)

def g1(p):
    return (20*p + 21/(p**2))/21

def g2(p):
    return p - (p**3 - 21)/(3*p**2)

def g3(p):
    return p - (p**4 - 21*p)/(p**3 - 21)

def g4(p):
    return (21/p)**0.5

funcoes = [g1,g2,g3,g4]

tol = 1e-6
max_iter = 20

for i,g in enumerate(funcoes):
    
    print(f"\nMétodo {i+1}")
    
    p = 1
    erro = 1
    n = 0
    erros = []
    
    while erro > tol and n < max_iter:
        
        p_novo = g(p)
        erro = abs(p_novo - valor_real)
        
        erros.append(erro)
        
        print(f"p{n+1} =",p_novo," erro =",erro)
        
        p = p_novo
        n += 1
    
    plt.plot(erros,label=f"g{i+1}")

plt.yscale("log")
plt.title("Convergência dos métodos")
plt.legend()
plt.grid()
plt.show()