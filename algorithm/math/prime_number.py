# 소수 prime number

# 나눠서 확인
def is_prime_num(num) :
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 에라토스테네스의 체
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