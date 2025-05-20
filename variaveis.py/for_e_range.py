for i in range(10, 20, 2):
    print(i) #Resultado: 10, 12, 14, 16, 18


# list = [1,2,3,4,5]
# for indice in range(0, len(list)):
#     print("Indice:", indice)
#     print("Indice:", list[indice])

#enumerate()
list_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(list_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")