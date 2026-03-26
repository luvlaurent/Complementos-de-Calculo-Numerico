# Questão 12

x_pontos = [0.698, 0.733, 0.768, 0.803]
y_pontos = [0.7661, 0.7432, 0.7193, 0.6946]

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

x = 0.75

aprox = lagrange(x_pontos, y_pontos, x)

print("Aproximação:", aprox)
print("Erro:", abs(0.7317 - aprox))
