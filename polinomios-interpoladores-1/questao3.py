import math

# --------------------------------------------------
# QUESTÃO 3
# Estimar limite do erro (Teorema)
# |f^(n+1)(ξ)| * |(x-x0)(x-x1)...| / (n+1)!
# --------------------------------------------------

xp = 0.45
x = [0,0.6,0.9]

# Exemplo com cos(x)
# f'''(x) = -cos(x) -> |f'''(x)| <= 1

M = 1  # limite da derivada

# Grau 2 → n=2
erro = (M/6)*abs((xp-x[0])*(xp-x[1])*(xp-x[2]))

print("Limitante do erro (cos):",erro)