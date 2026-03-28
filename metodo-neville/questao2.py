import numpy as np

# Método de Neville
def neville(xp, yp, x):
    n = len(xp)
    Q = [[0]*n for _ in range(n)]

    i = 0
    while i < n:
        Q[i][0] = yp[i]
        i += 1

    j = 1
    while j < n:
        i = 0
        while i < n - j:
            Q[i][j] = ((x - xp[i+j])*Q[i][j-1] - (x - xp[i])*Q[i+1][j-1])/(xp[i] - xp[i+j])
            i += 1
        j += 1

    return Q[0][n-1]

# a
xp = [8.1,8.3,8.6,8.7]
yp = [16.94410,17.56492,18.50515,18.82091]
print("1a:", neville(xp, yp, 8.4))

# b
xp = [-0.75,-0.5,-0.25,0]
yp = [-0.07181250,-0.02475000,0.33493750,1.10100000]
print("1b:", neville(xp, yp, -1/3))

# c
xp = [0.1,0.2,0.3,0.4]
yp = [0.62049958,-0.28398668,0.00660095,0.24842440]
print("1c:", neville(xp, yp, 0.25))

# d
xp = [0.6,0.7,0.8,1.0]
yp = [-0.17694460,0.01375227,0.22363362,0.65809197]
print("1d:", neville(xp, yp, 0.9))
