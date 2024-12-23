def fibonacci(x):
    if x==0:
        print(x)
        return 1
    if x==1:
        print(x)
        return 1
    else:
        print(x)
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(10))