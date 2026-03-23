import math
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# QUESTÃO 5
# Resolver com Newton (precisão 1e-4)
# --------------------------------------------------

def newton(f,df,p0,tol=1e-4,max_iter=50):
    
    p = p0
    n = 0
    
    while n < max_iter:
        
        if abs(df(p)) < 1e-12:
            print("Derivada zero")
            return None
        
        p_novo = p - f(p)/df(p)
        
        if abs(p_novo - p) < tol:
            return p_novo
        
        p = p_novo
        n += 1
    
    return p


# ---------------- A ----------------
fa = lambda x: x**3 - 2*x**2 - 5
dfa = lambda x: 3*x**2 - 4*x

# ---------------- B ----------------
fb = lambda x: x**3 + 3*x**2 - 1
dfb = lambda x: 3*x**2 + 6*x

# ---------------- C ----------------
fc = lambda x: x - math.cos(x)
dfc = lambda x: 1 + math.sin(x)

# ---------------- D ----------------
fd = lambda x: x - 0.8 - 0.2*math.sin(x)
dfd = lambda x: 1 - 0.2*math.cos(x)


ra = newton(fa,dfa,2)
rb = newton(fb,dfb,-2.5)
rc = newton(fc,dfc,1)
rd = newton(fd,dfd,1)

print("A)",ra)
print("B)",rb)
print("C)",rc)
print("D)",rd)


# -------- GRÁFICO (exemplo letra C) --------
x = np.linspace(0,2,400)
y = [fc(xi) for xi in x]

plt.plot(x,y)
plt.axhline(0)
plt.scatter(rc,0)

plt.title("Questão 5 - letra C")
plt.grid()
plt.show()