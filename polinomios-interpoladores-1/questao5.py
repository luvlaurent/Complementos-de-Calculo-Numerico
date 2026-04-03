# --------------------------------------------------
# QUESTÃO 5
# Interpolação com dados tabelados
# --------------------------------------------------

def lagrange(xi, yi, x):
    soma = 0
    for i in range(len(xi)):
        termo = yi[i]
        for j in range(len(xi)):
            if i != j:
                termo *= (x-xi[j])/(xi[i]-xi[j])
        soma += termo
    return soma


# -------- letra a --------
x = [8.1,8.3,8.6,8.7]
y = [16.94410,17.56492,18.50515,18.82091]
xp = 8.4

print("a)")
print("Grau1:",lagrange(x[:2],y[:2],xp))
print("Grau2:",lagrange(x[:3],y[:3],xp))
print("Grau3:",lagrange(x,y,xp))