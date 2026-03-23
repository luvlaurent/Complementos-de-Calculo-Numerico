import math

# --------------------------------------------------
# QUESTÃO 4
# --------------------------------------------------

g1 = lambda x: math.sqrt((2 - x**4)/3)
g2 = lambda x: (2 - 3*x**2)**0.25
g3 = lambda x: (2 - x**4)/(3*x)
g4 = lambda x: ((2 - 3*x**2)**(1/3))/x

funcoes = [g1,g2,g3,g4]

max_iter = 4

for i,g in enumerate(funcoes):
    
    print(f"\nMétodo {i+1}")
    
    p = 1
    
    for n in range(max_iter):
        try:
            p = g(p)
            print(f"p{n+1} =",p)
        except:
            print("Iteração inválida (domínio ou divisão por zero)")
            p = float('nan')