import numpy as np
import matplotlib.pyplot as plt

# FUNÇÕES BASE (NEWTON)

def diferencas_divididas(x, y):
    """
    Constrói a tabela de diferenças divididas usada no método de Newton.
    Essa tabela armazena os coeficientes do polinômio interpolador.
    """
    
    n = len(x)  # número de pontos fornecidos
    
    # Cria uma matriz n x n preenchida com zeros
    tabela = np.zeros((n, n))
    
    # A primeira coluna da tabela é composta pelos valores de f(x)
    # Coloca os valores de y em todas as linhas da coluna 0 da matriz tabela
    tabela[:, 0] = y  

    # Preenche o restante da tabela com a fórmula das diferenças divididas
    for j in range(1, n):              # percorre as colunas
        for i in range(n - j):         # percorre as linhas
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (x[i+j] - x[i])

    return tabela  # retorna a tabela completa


def newton(x, tabela, valor):
    """
    Avalia o polinômio interpolador de Newton em um ponto específico.
    """
    
    n = len(x)  # número de pontos
    
    # Começa com o primeiro coeficiente (f[x0])
    resultado = tabela[0][0]
    
    # Variável que armazena o produto acumulado (x - x0)(x - x1)...
    produto = 1.0

    # Loop que constrói o polinômio termo a termo
    for i in range(1, n):
        produto *= (valor - x[i-1])  # atualiza o produto acumulado
        resultado += tabela[0][i] * produto  # adiciona o termo ao resultado

    return resultado

# CÁLCULO DIRETO DO POLINÔMIO

# Valor onde queremos avaliar a função interpolada
x = 0.75

# Aqui o polinômio de Newton já foi montado manualmente:

P = 1 \
    + 4*x \
    + 4*x*(x - 0.25) \
    + (16/3)*x*(x - 0.25)*(x - 0.5)

# Cada termo corresponde a um grau do polinômio:
# - 1 → termo constante
# - 4x → termo linear
# - 4x(x - 0.25) → termo de grau 2
# - (16/3)x(x - 0.25)(x - 0.5) → termo de grau 3


# Exibe o resultado da interpolação no ponto x = 0.75
print("f(0.75) =", P)