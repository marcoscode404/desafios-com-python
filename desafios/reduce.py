from functools import reduce

def soma(x, y):
    return x+ y

list = [1,3,5,10,20]

soma = reduce(soma, list)
print(soma)