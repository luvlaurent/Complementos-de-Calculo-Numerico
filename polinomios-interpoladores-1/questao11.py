# Questão 11

xp = [1.00, 1.05, 1.10, 1.15]
yp = [0.1924, 0.2414, 0.2933, 0.3492]

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

print("11:", lagrange(xp, yp, 1.09))
