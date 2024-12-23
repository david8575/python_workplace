n = int(input())

order = list(map(int, input().split()))
count = 0

main = [i+1 for i in range(n)]
sub = []
sub_size = 0
for i in range(n):
    if order[i] == main[0]:
        count+=1
        main.pop(0)
    else:
        if sub_size != 0:
            if sub[-1] == order[i]:
                count+=1
                sub.pop()
            else:
                sub.append(main.pop(0))
                break

print(count)