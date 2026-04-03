# --------------------------------------------------
# QUESTÃO 2
# 4 iterações com controle
# --------------------------------------------------

g1 = lambda x: (3 + x - 2*x**2)**(1/4)
g2 = lambda x: ((x + 3 - x**4)/2)**0.5
g3 = lambda x: ((x + 3)/(x**2 + 2))**0.5
g4 = lambda x: (3*x**4 + 2*x**2 + 3)/(4*x**3 + 4*x - 1)

funcoes = [g1,g2,g3,g4]
max_iter = 4

for i,g in enumerate(funcoes):
    
    print(f"\nFunção g{i+1}")
    
    p = 1
    
    for n in range(max_iter):
        p = g(p)
        print(f"p{n+1} =",p)