def sqrt(a):
    x = a / 2
    error = 0.00001
    
    while True:
        y = x
        x = (x + a / x) / 2
        if abs(y - x) < error:
            break
            
    return x

