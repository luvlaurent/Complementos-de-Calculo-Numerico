import sympy as sp

x1 = sp.Symbol('x1')

def f(x):
    return sp.sqrt(x - x**2)

def P(x):
    xp = [0, x1, 1]
    yp = [f(0), f(x1), f(1)]

    s = 0
    i = 0
    while i < 3:
        p = yp[i]
        j = 0
        while j < 3:
            if i != j:
                p *= (x - xp[j])/(xp[i] - xp[j])
            j += 1
        s += p
        i += 1
    return s

eq = f(0.5) - P(0.5) + 0.25
print("x1 =", sp.solve(eq, x1))
