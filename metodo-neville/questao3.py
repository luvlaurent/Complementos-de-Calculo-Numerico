import numpy as np

real = np.sqrt(3)

# a
print("3a")
def f(x): return 3**x
xp = [-2,-1,0,1,2]
yp = [f(xp[0]),f(xp[1]),f(xp[2]),f(xp[3]),f(xp[4])]
Q = neville(xp, yp, 0.5)
aprox_a = Q[0][4]
print("Aproximação:", aprox_a)

# b
print("\n3b")
def f(x): return np.sqrt(x)
xp = [0,1,2,4,5]
yp = [f(xp[0]),f(xp[1]),f(xp[2]),f(xp[3]),f(xp[4])]
Q = neville(xp, yp, 3)
aprox_b = Q[0][4]
print("Aproximação:", aprox_b)

# c
print("\n3c")
print("Valor real:", real)

erro_a = abs(real - aprox_a)
erro_b = abs(real - aprox_b)

print("Erro (a):", erro_a)
print("Erro (b):", erro_b)

print("\nConclusão:")
print("A melhor aproximação é a que tem menor erro.")
