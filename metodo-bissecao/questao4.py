import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 4
# Resolver x^4 - 2x^3 - 4x^2 + 4x + 4 = 0
# com precisão 10^-2 nos intervalos:
# a) [-2,-1] b) [0,2] c) [2,3] d) [-1,0]
# --------------------------------------------------

def f(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

def bissecao(f,a,b,tol=1e-2):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


ra = bissecao(f,-2,-1)
rb = bissecao(f,0,2)
rc = bissecao(f,2,3)
rd = bissecao(f,-1,0)

print("A)",ra)
print("B)",rb)
print("C)",rc)
print("D)",rd)


x = np.linspace(-2,3,400)
y = f(x)

plt.plot(x,y)
plt.axhline(0)
plt.scatter([ra,rb,rc,rd],[0,0,0,0])

plt.title("Questão 4")
plt.grid()
plt.show()