import math

# --------------------------------------------------
# QUESTÃO 4
# Mesmo processo da questão 3 para novos pontos
# --------------------------------------------------

xp = 1.4
x = [1,1.25,1.6]

# exemplo com e^(2x)-x
# derivada terceira cresce rápido → usar estimativa

M = 100  # aproximação conservadora

erro = (M/6)*abs((xp-x[0])*(xp-x[1])*(xp-x[2]))

print("Limitante aproximado:",erro)