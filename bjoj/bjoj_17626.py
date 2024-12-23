import math
n = int(input())

def find_lagrange_squares(n):
    for i in range(int(math.isqrt(n)) + 1):
        for j in range(int(math.isqrt(n - i * i)) + 1):
            for k in range(int(math.isqrt(n - i * i - j * j)) + 1):
                l = math.isqrt(n - i * i - j * j - k * k)
                if i * i + j * j + k * k + l * l == n:
                    return [i, j, k, l]
    return []

find_lagrange_squares(len(n))
