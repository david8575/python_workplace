# 최대공약수 최소공배수 GCD LCM

# gcd
def gcd(a,b):
    if b == 0:
        return a 
    else:
        return gcd(b, a%b)
    
# lcm
def lcm(a, b):
    return a * b // gcd(a, b)