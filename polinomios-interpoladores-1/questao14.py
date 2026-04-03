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
def fa(x): return np.exp(-x)*np.sin(3*x)
xp = [0,np.pi/6,np.pi/4]
yp = [fa(xp[0]),fa(xp[1]),fa(xp[2])]
print("14a:", lagrange(xp, yp, 0.2))

# b)
def fb(x): return np.log10(x)
xp = [3,3.2,3.5]
yp = [fb(xp[0]),fb(xp[1]),fb(xp[2])]
print("14b:", lagrange(xp, yp, 3.1))

# c)
def fc(x): return np.exp(x)+np.exp(-x)
xp = [-0.3,0,0.3]
yp = [fc(xp[0]),fc(xp[1]),fc(xp[2])]
print("14c:", lagrange(xp, yp, 0.1))

# d)
def fd(x): return np.cos(2*np.log(3*x))
xp = [0.1,0.3,0.5,1.0]
yp = [fd(xp[0]),fd(xp[1]),fd(xp[2]),fd(xp[3])]
print("14d:", lagrange(xp, yp, 0.4))
