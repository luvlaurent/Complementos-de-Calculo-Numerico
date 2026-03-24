import math

def newton(f, df, p0, tol=1e-6, max_iter=100):
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
print("QUESTÃO 9")
print("=" * 60)

# 9) f(x) = ln(x^2+1) - e^(0.4x) cos(πx)
print("\n9) f(x) = ln(x^2+1) - e^(0.4x) cos(πx)\n")

def f9(x):
    return math.log(x**2 + 1) - math.exp(0.4*x) * math.cos(math.pi*x)

def df9(x):
    termo1 = (2*x) / (x**2 + 1)
    termo2 = 0.4 * math.exp(0.4*x) * math.cos(math.pi*x)
    termo3 = math.pi * math.exp(0.4*x) * math.sin(math.pi*x)
    return termo1 - (termo2 - termo3)

# 9a) Zero negativo
print("9a) Zero negativo:")
raiz9a = newton(f9, df9, -0.5)
print(f"Raiz: {raiz9a:.8f}\n")

# 9b) Quatro menores zeros positivos
print("9b) Quatro menores zeros positivos:")
chutes_pos = [0.2, 0.9, 1.9, 2.8]
for i, chute in enumerate(chutes_pos, 1):
    raiz = newton(f9, df9, chute)
    print(f"{i}º zero positivo: {raiz:.8f}")

print()

# 9c) Aproximação para o n-ésimo zero positivo
print("9c) Aproximação para o n-ésimo zero positivo:")
print("Observando o gráfico, os zeros ocorrem aproximadamente quando")
print("cos(πx) = 0, ou seja, x ≈ n + 0.5 para n ≥ 1.")
print("Sugestão: chute inicial = n + 0.5\n")

# 9d) 25º menor zero positivo
print("9d) 25º menor zero positivo:")
chute_25 = 25.5
raiz9d = newton(f9, df9, chute_25)
print(f"Raiz: {raiz9d:.8f}")
