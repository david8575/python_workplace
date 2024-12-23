def f(x):
    return -9.96762 + 2.374100 * x

y1 = f(5)
y2 = f(6)
y3 = f(7)
y4 = f(6)
y5 = f(9)
y6 = f(8)
y7 = f(7)
y8 = f(10)
y9 = f(12)
y10 = f(12)

e1 = 0 - y1
e2 = 2 - y2
e3 = 4 - y3
e4 = 6 - y4
e5 = 9 - y5
e6 = 11 - y6
e7 = 12 - y7
e8 = 15 - y8
e9 = 17 - y9
e10 = 19 - y10

print(f"estimated : {y1}, erroe : {e1}")
print(f"estimated : {y2}, erroe : {e2}")
print(f"estimated : {y3}, erroe : {e3}")
print(f"estimated : {y4}, erroe : {e4}")
print(f"estimated : {y5}, erroe : {e5}")
print(f"estimated : {y6}, erroe : {e6}")
print(f"estimated : {y7}, erroe : {e7}")
print(f"estimated : {y8}, erroe : {e8}")
print(f"estimated : {y9}, erroe : {e9}")
print(f"estimated : {y10}, erroe : {e10}")

