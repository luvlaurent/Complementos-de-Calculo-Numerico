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
print("QUESTÃO 10")
print("=" * 60)

# 10) f(x) = 1/2 + x^2/4 - x sen x - (1/2) cos 2x
print("\n10) f(x) = 1/2 + x^2/4 - x sen x - (1/2) cos 2x\n")

def f10(x):
    return 0.5 + 0.25*x**2 - x*math.sin(x) - 0.5*math.cos(2*x)

def df10(x):
    return 0.5*x - math.sin(x) - x*math.cos(x) + math.sin(2*x)

# 10a) p0 = π/2
print("10a) p0 = π/2:")
raiz10a = newton(f10, df10, math.pi/2)
print(f"Raiz: {raiz10a:.8f}")

print("\nExplicação do comportamento anômalo:")
print("O método de Newton apresenta convergência lenta porque a derivada")
print("da função se aproxima de zero próximo à raiz, fazendo com que as")
print("iterações oscilem ou convirjam lentamente.\n")

# 10b) p0 = 5π
print("10b) p0 = 5π:")
raiz10b = newton(f10, df10, 5*math.pi)
print(f"Raiz: {raiz10b:.8f}")

# 10c) p0 = 10π
print("\n10c) p0 = 10π:")
raiz10c = newton(f10, df10, 10*math.pi)
print(f"Raiz: {raiz10c:.8f}")
