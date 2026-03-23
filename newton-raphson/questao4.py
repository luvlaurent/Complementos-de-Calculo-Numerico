import math

# --------------------------------------------------
# QUESTÃO 4
# f(x) = -x^3 - cos(x)
# p0 = -1, p1 = 0
# calcular p3
# --------------------------------------------------

def f(x):
    return -x**3 - math.cos(x)


# -------- SECANTE --------
def secante(p0,p1,n_iter):
    
    for i in range(n_iter):
        
        if abs(f(p1)-f(p0)) < 1e-12:
            print("Erro numérico")
            return
        
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
secante(-1,0,2)

print("\nFalsa posição:")
falsa_posicao(-1,0,2)