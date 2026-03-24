import math

def newton(f, df, p0, tol=1e-5, max_iter=100):
    p = p0
    for i in range(max_iter):
        fp = f(p)
        dfp = df(p)
        if abs(dfp) < 1e-12:
            print(f"  Derivada zero em x = {p:.6f}")
            return None
        p_next = p - fp / dfp
        if abs(p_next - p) < tol:
            print(f"  Convergiu após {i+1} iterações")
            return p_next
        p = p_next
    print(f"  Máximo de iterações atingido")
    return p

print("Questão 7")
print("Equação: 4x² - e^x - e^(-x) = 0")
print("Duas soluções positivas\n")

def f7(x):
    return 4*x**2 - math.exp(x) - math.exp(-x)

def df7(x):
    return 8*x - math.exp(x) + math.exp(-x)

# a) p0 = -10
print("a) p0 = -10")
raiz_a = newton(f7, df7, -10)
if raiz_a:
    print(f"   Raiz: {raiz_a:.8f}\n")

# b) p0 = -5
print("b) p0 = -5")
raiz_b = newton(f7, df7, -5)
if raiz_b:
    print(f"   Raiz: {raiz_b:.8f}\n")

# c) p0 = -3
print("c) p0 = -3")
raiz_c = newton(f7, df7, -3)
if raiz_c:
    print(f"   Raiz: {raiz_c:.8f}\n")

# d) p0 = -1
print("d) p0 = -1")
raiz_d = newton(f7, df7, -1)
if raiz_d:
    print(f"   Raiz: {raiz_d:.8f}\n")

# e) p0 = 0
print("e) p0 = 0")
raiz_e = newton(f7, df7, 0)
if raiz_e:
    print(f"   Raiz: {raiz_e:.8f}\n")
else:
    print("   Derivada zero em x = 0, método falha\n")

# f) p0 = 1
print("f) p0 = 1")
raiz_f = newton(f7, df7, 1)
if raiz_f:
    print(f"   Raiz: {raiz_f:.8f}\n")

# g) p0 = 3
print("g) p0 = 3")
raiz_g = newton(f7, df7, 3)
if raiz_g:
    print(f"   Raiz: {raiz_g:.8f}\n")

# h) p0 = 5
print("h) p0 = 5")
raiz_h = newton(f7, df7, 5)
if raiz_h:
    print(f"   Raiz: {raiz_h:.8f}\n")

# i) p0 = 10
print("i) p0 = 10")
raiz_i = newton(f7, df7, 10)
if raiz_i:
    print(f"   Raiz: {raiz_i:.8f}\n")

print("Resumo:")
print(f"Com p0 = -10, -5, -3, -1 convergiu para x = {raiz_a:.8f}")
print(f"Com p0 = 0 não convergiu (derivada zero)")
print(f"Com p0 = 1 convergiu para x = {raiz_f:.8f}")
print(f"Com p0 = 3 convergiu para x = {raiz_g:.8f}")
print(f"Com p0 = 5 convergiu para x = {raiz_h:.8f}")
print(f"Com p0 = 10 convergiu para x = {raiz_i:.8f}")
print(f"\nA equação tem duas raízes positivas: aproximadamente {raiz_f:.5f} e {raiz_g:.5f}")
