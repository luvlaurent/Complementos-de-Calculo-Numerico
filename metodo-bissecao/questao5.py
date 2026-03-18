import math
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 5
# Resolver numericamente as equações:
# a) x - 2^-x = 0
# b) e^x - x^2 + 3x - 2 = 0
# c) 2x cos(2x) - (x+1)^2 = 0
# d) x cos x - 2x^2 + 3x - 1 = 0
# --------------------------------------------------

def bissecao(f,a,b,tol=1e-6):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


# --------- A ---------
fa = lambda x: x - 2**(-x)
ra = bissecao(fa,0,1)

# --------- B ---------
fb = lambda x: math.exp(x) - x**2 + 3*x - 2
rb = bissecao(fb,0,1)

# --------- C ---------
fc = lambda x: 2*x*math.cos(2*x) - (x+1)**2
rc1 = bissecao(fc,-3,-2)
rc2 = bissecao(fc,-1,0)

# --------- D ---------
fd = lambda x: x*math.cos(x) - 2*x**2 + 3*x - 1
rd1 = bissecao(fd,0.2,0.3)
rd2 = bissecao(fd,1.2,1.3)

print("A)",ra)
print("B)",rb)
print("C)",rc1,rc2)
print("D)",rd1,rd2)