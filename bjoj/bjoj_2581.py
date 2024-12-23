def eratosthenes(num):
    count_primes = [True] * (num+1)
    count_primes[0] = False
    count_primes[1] = False

    for i in range(2, int(num**0.5)+1):
        if count_primes[i]:
            for j in range(i*i, num+1, i):
                count_primes[j] = False
    
    primes = []
    for i in range(2, num+1):
        if count_primes[i]:
            print(i)
            
print(eratosthenes(10))