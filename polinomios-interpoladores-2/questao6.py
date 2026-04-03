import numpy as np

def hermite(x, y, dy):
    n = len(x)
    z = np.zeros(2*n)
    Q = np.zeros((2*n, 2*n))

    for i in range(n):
        z[2*i] = z[2*i+1] = x[i]
        Q[2*i][0] = Q[2*i+1][0] = y[i]
        Q[2*i+1][1] = dy[i]

        if i != 0:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])

    for i in range(2, 2*n):
        for j in range(2, i+1):
            Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

    return z, Q


def avalia_hermite(z, Q, x):
    n = len(z)
    resultado = Q[0][0]
    produto = 1

    for i in range(1, n):
        produto *= (x - z[i-1])
        resultado += Q[0][i] * produto

    return resultado


# Exemplo (6a)
x = np.array([8.3, 8.6])
y = np.array([17.56492, 18.50515])
dy = np.array([3.116256, 3.151762])

z, Q = hermite(x, y, dy)

valor = 8.4
p = avalia_hermite(z, Q, valor)

print("Hermite:", p)