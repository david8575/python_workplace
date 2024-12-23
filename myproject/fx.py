def f(x):
    return -0.1*(x**4) - 0.15*(x**3) - 0.5*(x**2) - 0.25*x +1.2

x = 0.5
h = 0.25
print((f(x+h)-f(h))/h)
print((f(x)-f(x-h))/h)
print((f(x+h)-f(x-h))/h)