import math

# Método de Newton-Raphson
def newton(f, df, p0, tol=1e-5, max_iter=100):
    p = p0
    for i in range(max_iter):
        fp = f(p)
        dfp = df(p)
        if dfp == 0:
            print("Derivada zero. Método falha.")
            return None
        p_next = p - fp / dfp
        if abs(p_next - p) < tol:
            return p_next
        p = p_next
    print("Número máximo de iterações atingido.")
    return p

# 6a) e^x + 2^{-x} + 2 cos x - 6 = 0, [1, 2]
def f6a(x):
    return math.exp(x) + 2**(-x) + 2*math.cos(x) - 6

def df6a(x):
    return math.exp(x) - 2**(-x)*math.log(2) - 2*math.sin(x)

raiz6a = newton(f6a, df6a, 1.5)
print(f"6a) Raiz aproximada: {raiz6a:.6f}")

# 6b) ln(x-1) + cos(x-1) = 0, [1.3, 2]
def f6b(x):
    return math.log(x-1) + math.cos(x-1)

def df6b(x):
    return 1/(x-1) - math.sin(x-1)

raiz6b = newton(f6b, df6b, 1.5)
print(f"6b) Raiz aproximada: {raiz6b:.6f}")

# 6c) 2x cos(2x) - (x-2)^2 = 0, [2, 3] e [3, 4]
def f6c(x):
    return 2*x*math.cos(2*x) - (x-2)**2

def df6c(x):
    return 2*math.cos(2*x) - 4*x*math.sin(2*x) - 2*(x-2)

raiz6c1 = newton(f6c, df6c, 2.5)
raiz6c2 = newton(f6c, df6c, 3.5)
print(f"6c) Raiz em [2,3]: {raiz6c1:.6f}")
print(f"6c) Raiz em [3,4]: {raiz6c2:.6f}")

# 6d) (x-2)^2 - ln x = 0, [1,2] e [e, 4]
def f6d(x):
    return (x-2)**2 - math.log(x)

def df6d(x):
    return 2*(x-2) - 1/x

raiz6d1 = newton(f6d, df6d, 1.5)
raiz6d2 = newton(f6d, df6d, 3.0)
print(f"6d) Raiz em [1,2]: {raiz6d1:.6f}")
print(f"6d) Raiz em [e,4]: {raiz6d2:.6f}")

# 6e) e^x - 3x^2 = 0, [0,1] e [3,5]
def f6e(x):
    return math.exp(x) - 3*x**2

def df6e(x):
    return math.exp(x) - 6*x

raiz6e1 = newton(f6e, df6e, 0.5)
raiz6e2 = newton(f6e, df6e, 4.0)
print(f"6e) Raiz em [0,1]: {raiz6e1:.6f}")
print(f"6e) Raiz em [3,5]: {raiz6e2:.6f}")

# 6f) sin x - e^{-x} = 0, [0,1], [3,4], [6,7]
def f6f(x):
    return math.sin(x) - math.exp(-x)

def df6f(x):
    return math.cos(x) + math.exp(-x)

raiz6f1 = newton(f6f, df6f, 0.5)
raiz6f2 = newton(f6f, df6f, 3.5)
raiz6f3 = newton(f6f, df6f, 6.5)
print(f"6f) Raiz em [0,1]: {raiz6f1:.6f}")
print(f"6f) Raiz em [3,4]: {raiz6f2:.6f}")
print(f"6f) Raiz em [6,7]: {raiz6f3:.6f}")
