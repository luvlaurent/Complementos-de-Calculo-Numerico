import math

# --------------------------------------------------
# QUESTÃO 2
# f(x) = -x^3 - cos(x)
# p0 = -1
# calcular p2
# verificar p0 = 0
# --------------------------------------------------

def f(x):
    return -x**3 - math.cos(x)

def df(x):
    return -3*x**2 + math.sin(x)

def newton(p0, n_iter):
    
    p = p0
    
    for i in range(n_iter):
        
        if abs(df(p)) < 1e-12:
            print("Derivada zero -> método falha")
            return
        
        p = p - f(p)/df(p)
        print(f"p{i+1} =",p)


# -------- p0 = -1 --------
print("Com p0 = -1")
newton(-1,2)


# -------- p0 = 0 --------
print("\nTestando p0 = 0")
newton(0,2)