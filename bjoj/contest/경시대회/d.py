a,b,c = map(int, input().split())

plans = []
for i in range(3):
    plans.append(input())

for plan in plans:
    count = 0
    count_a = 0
    count_b = 0
    count_c = 0

    for i in range(len(plan)):
        if plan[i] == 'A':
            count_a += 1
        elif plan[i] == 'B':
            count_b += 1
        elif plan[i] == 'C':
            count_c += 1
    
    if (a != count_a or b != count_b or c != count_c):
        print("Candy is not enough!")
    else:
        check = 0
        for i in range(len(plan)-1):
            if plan[i] == plan[i+1]:
                count+=1
                if count == 2:
                    check = 1
            else:
                count = 0 
        if (check):
            print("Tired of candy!")
        else:
            print("Tastes good!")
        