import math
def f(x):
    ans = ans = x**5 -16.05*(x**4) + 88.75*(x**3) - 192.0375*(x**2) + 116.35*x + 31.6875
    return ans

n = float(input())
k = 0.05

while(True):
    n = float(input())
    result = n - k * (f(n) / (f(n+k*n) - f(n)))
    print(f"{n} - {k*f(n)} / ({f(n+k*n)} - {f(n)}) = {n - k * (f(n) / (f(n+k*n) - f(n)))}")
    print(f"error = {abs(n-result)}")
    if abs(n-result) < 0.01:
        break