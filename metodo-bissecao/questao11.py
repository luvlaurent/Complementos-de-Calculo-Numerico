def f(x):
    return (x+2)*(x+1)*x*(x-1)**3*(x-2)

def bisseccao(f, a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b)/2

        if abs(f(c)) < tol or (b - a)/2 < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c

print("a)", bisseccao(f, -3, 1, 1e-5, 100))
print("b)", bisseccao(f, -2.5, 3, 1e-5, 100))
print("c)", bisseccao(f, -1.75, 1.5, 1e-5, 100))
print("d)", bisseccao(f, -1.5, 1.75, 1e-5, 100))
