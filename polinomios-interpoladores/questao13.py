import numpy as np

def lagrange(xp, yp, x):
    i = 0
    s = 0
    while i < len(xp):
        p = yp[i]
        j = 0
        while j < len(xp):
            if i != j:
                p *= (x - xp[j])/(xp[i] - xp[j])
            j += 1
        s += p
        i += 1
    return s

# a)
def fa(x): return np.exp(2*x)*np.cos(3*x)
xp = [0,0.3,0.6]
yp = [fa(xp[0]),fa(xp[1]),fa(xp[2])]
print("13a:", lagrange(xp, yp, 0.2))

# b)
def fb(x): return np.sin(np.log(x))
xp = [2.0,2.4,2.6]
yp = [fb(xp[0]),fb(xp[1]),fb(xp[2])]
print("13b:", lagrange(xp, yp, 2.2))

# c)
def fc(x): return np.log(x)
xp = [1,1.1,1.3,1.4]
yp = [fc(xp[0]),fc(xp[1]),fc(xp[2]),fc(xp[3])]
print("13c:", lagrange(xp, yp, 1.2))

# d)
def fd(x): return np.cos(x)+np.sin(x)
xp = [0,0.25,0.5,1.0]
yp = [fd(xp[0]),fd(xp[1]),fd(xp[2]),fd(xp[3])]
print("13d:", lagrange(xp, yp, 0.3))
