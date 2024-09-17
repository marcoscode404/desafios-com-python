def externa():
    z = 13
    print(z)
    print(f'valor de z = {z}')
    def interna():
        y = 14
        print(f'valor de y = {y}')
    interna()
x = 10
externa()
print(f'valor de x = {x}')