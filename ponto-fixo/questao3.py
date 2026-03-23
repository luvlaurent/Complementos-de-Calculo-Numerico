import math

# --------------------------------------------------
# QUESTÃO 3 (CORRIGIDA)
# Tratamento de erro numérico
# --------------------------------------------------

g1 = lambda x: (x**3 + 1)/2
g2 = lambda x: 2/x - 1/(x**2)
g3 = lambda x: math.sqrt(2 - 1/x)
g4 = lambda x: -(1 - 2*x)**(1/3)

funcoes = [g1,g2,g3,g4]

max_iter = 4

for i,g in enumerate(funcoes):
    
    print(f"\nMétodo {i+1}")
    
    p = 0.5
    
    for n in range(max_iter):
        
        try:
            p_novo = g(p)
            
            # Verificação de problema numérico
            if abs(p) < 1e-12:
                print(f"p{n+1} = indefinido (divisão por zero)")
                break
            
            if isinstance(p_novo, complex):
                print(f"p{n+1} = número complexo (método inválido)")
                break
            
            print(f"p{n+1} =",p_novo)
            
            p = p_novo
            
        except:
            print(f"p{n+1} = erro numérico (método divergente)")
            break