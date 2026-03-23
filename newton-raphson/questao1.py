import math

# --------------------------------------------------
# QUESTÃO 1
# f(x) = x^2 - 6
# p0 = 1
# Calcular p2 usando Newton
# --------------------------------------------------

def f(x):
    return x**2 - 6

def df(x):
    return 2*x

def newton(p0, n_iter):
    
    p = p0
    
    for i in range(n_iter):
        p = p - f(p)/df(p)
        print(f"p{i+1} =",p)
    
    return p


# cálculo até p2
newton(1,2)