n = int(input())
found = False
for i in range(n // 2+1):
    if (n-2*i) % 5 == 0:
        found = True
        print(i+(n-2*i)//5)
        break
        
if not found:
    print(-1)