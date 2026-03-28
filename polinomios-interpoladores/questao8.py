import numpy as np

def lagrange(xp, yp, x):
    n = len(xp)
    i = 0
    s = 0

    while i < n:
        p = yp[i]
        j = 0
        while j < n:
            if i != j:
                p *= (x - xp[j])/(xp[i] - xp[j])
            j += 1
        s += p
        i += 1
    return s

x = 0.43
xp = [0, 0.25, 0.5]

# a)
def fa(x): return np.exp(x)
yp = [fa(0), fa(0.25), fa(0.5)]
print("8a:", abs(fa(x) - lagrange(xp, yp, x)))

# b)
def fb(x): return x**4 - x**3 + x**2 - x + 1
yp = [fb(0), fb(0.25), fb(0.5)]
print("8b:", abs(fb(x) - lagrange(xp, yp, x)))

# c)
def fc(x): return x**2*np.cos(x) - 3*x
yp = [fc(0), fc(0.25), fc(0.5)]
print("8c:", abs(fc(x) - lagrange(xp, yp, x)))

# d)
def fd(x): return np.log(np.exp(x)+2)
yp = [fd(0), fd(0.25), fd(0.5)]
print("8d:", abs(fd(x) - lagrange(xp, yp, x)))
