cores = ['azul','verde','amarelo']
numeros = [1,2,3]
for cor in cores:
    for numero in numeros:
       print(f'{cor.capitalize()} - {numero}')


print('-------------------------------------------------')

alimentos = ['arroz','feijão','batata']
for indice,alimento in enumerate(alimentos):
    print(f'{indice} -> {alimento}')