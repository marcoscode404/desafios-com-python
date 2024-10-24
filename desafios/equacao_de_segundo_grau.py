import math

a = 1
b = -5
c = 6

delta = b**2 - 4*a*c
if delta < 0:
    print('sem solução real')
else: 
    x1 = (-b + math.sqrt(delta) / (2 * a))
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'As raízes são: {x1} e {x2}')