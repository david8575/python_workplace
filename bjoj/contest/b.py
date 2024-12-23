n = int(input())

for _ in range(n):
    a, b = map(int,input().split())

    addStem, addLeaf = 0, 0

    while a > 0 and b >= 3:
        a -=1
        b -=3

    if b > 0 and b < 3:
        addStem = 1
        b += 1
    
    if b >= 3:
        addStem += b//3
        b %= 3
    
    if a > 0:
        addLeaf = a * 3

    print(addStem+addLeaf)