import math

# --------------------------------------------------
# QUESTÃO 6
# Resolver com precisão 10^-5:
# a) 3x - e^x = 0
# b) 2x + 3cos(x) - e^x = 0
# c) x^2 - 4x + 4 - ln(x) = 0
# d) x + 1 - 2sen(pi x) = 0
# --------------------------------------------------

def bissecao(f,a,b,tol=1e-5):
    
    while (b-a)/2 > tol:
        p = (a+b)/2
        
        if f(a)*f(p) < 0:
            b = p
        else:
            a = p
            
    return (a+b)/2


fa = lambda x: 3*x - math.exp(x)
fb = lambda x: 2*x + 3*math.cos(x) - math.exp(x)
fc = lambda x: x**2 - 4*x + 4 - math.log(x)
fd = lambda x: x + 1 - 2*math.sin(math.pi*x)

print("A)",bissecao(fa,1,2))
print("B)",bissecao(fb,0,1))
print("C)",bissecao(fc,1,2),bissecao(fc,2,4))
print("D)",bissecao(fd,0,0.5),bissecao(fd,0.5,1))