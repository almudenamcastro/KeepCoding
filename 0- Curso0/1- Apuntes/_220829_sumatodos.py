def sumatodos(n):
    total=0
    for i in range(n+1):
        total += i
    return total

def cuadrado(i):
    return i*i

def sumatorio(n, function=None):
    total=0
    for i in range(n+1):
        if function == None:
            total += i
        else:
            total += function(i)
    return total

Q = lambda i: i**2
