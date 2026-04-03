# --------------------------------------------------
# QUESTÃO 6
# Mesmo formato da questão 5
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


# exemplo letra a
x = [0,0.25,0.5,0.75]
y = [1,1.64872,2.71828,4.48169]
xp = 0.43

print("a)")
print("Grau1:",lagrange(x[:2],y[:2],xp))
print("Grau2:",lagrange(x[:3],y[:3],xp))
print("Grau3:",lagrange(x,y,xp))