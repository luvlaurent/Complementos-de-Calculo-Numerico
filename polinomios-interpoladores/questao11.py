# Questão 11

x_pontos = [1.00, 1.05, 1.10, 1.15]
y_pontos = [0.1924, 0.2414, 0.2933, 0.3492]

def lagrange(x_pontos, y_pontos, x):
    n = len(x_pontos)
    i = 0
    resultado = 0

    while i < n:
        termo = y_pontos[i]
        j = 0
        while j < n:
            if i != j:
                termo *= (x - x_pontos[j])/(x_pontos[i] - x_pontos[j])
            j += 1
        resultado += termo
        i += 1

    return resultado

x = 1.09

print("Aproximação:", lagrange(x_pontos, y_pontos, x))
