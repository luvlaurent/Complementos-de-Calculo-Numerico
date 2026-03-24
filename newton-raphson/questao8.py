import math

def newton(f, df, p0, tol=1e-5, max_iter=100):
    """Método de Newton-Raphson"""
    p = p0
    for i in range(max_iter):
        fp = f(p)
        dfp = df(p)
        if dfp == 0:
            print(f"Erro: derivada zero em x = {p}")
            return None
        p_next = p - fp / dfp
        if abs(p_next - p) < tol:
            return p_next
        p = p_next
    return p

print("=" * 60)
print("QUESTÃO 8")
print("=" * 60)

# 8) x^2 - 10 cos x = 0
print("\n8) x^2 - 10 cos x = 0")
print("Soluções esperadas: ±1.3793646\n")

def f8(x):
    return x**2 - 10*math.cos(x)

def df8(x):
    return 2*x + 10*math.sin(x)

# 8a) p0 = -100
print("8a) p0 = -100")
raiz8a = newton(f8, df8, -100)
print(f"Raiz: {raiz8a:.8f}")

# 8b) p0 = -50
print("\n8b) p0 = -50")
raiz8b = newton(f8, df8, -50)
print(f"Raiz: {raiz8b:.8f}")

# 8c) p0 = -25
print("\n8c) p0 = -25")
raiz8c = newton(f8, df8, -25)
print(f"Raiz: {raiz8c:.8f}")

# 8d) p0 = 25
print("\n8d) p0 = 25")
raiz8d = newton(f8, df8, 25)
print(f"Raiz: {raiz8d:.8f}")

# 8e) p0 = 50
print("\n8e) p0 = 50")
raiz8e = newton(f8, df8, 50)
print(f"Raiz: {raiz8e:.8f}")

# 8f) p0 = 100
print("\n8f) p0 = 100")
raiz8f = newton(f8, df8, 100)
print(f"Raiz: {raiz8f:.8f}")
