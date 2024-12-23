import math
def f(x):
    ans = 7*math.sin(x)*math.exp(-x) - 1
    return ans

x1, x2 = map(float, input().split())

print(f(x1))
print(f(x2))

print(x1-x2)
print(f(x1)- f(x2))

print(x1 - f(x1) * ( (x1-x2) / ( f(x1)-f(x2) ) ) )
print(f"{x1} - {f(x1)}(({x1-x2}) / ({f(x1)-f(x2)})) = {x1 - f(x1) * ( (x1-x2) / ( f(x1)-f(x2) ) ) }")