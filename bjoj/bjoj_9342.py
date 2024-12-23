n = int(input())

for _ in range(n):
    gene = input()
    
    if len(gene) < 3:
        print("Good")
        continue
    
    if gene[0] != 'A':
        if gene[0] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
            print("Good")
            continue
        gene = gene[1:]
        
    if gene[-1] != 'C':
        if gene[-1] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
            print("Good")
            continue
        gene = gene[:-1]
        
    