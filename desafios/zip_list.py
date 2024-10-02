list1 = [1,2,3,4,5]
list2 = ["abacate", "cobra", "gato", "bola", "bolo"]
list3 = ["R$ 2,00", "R$ 500,00", "R$ 200,00", "R$ 100,00", "R$ 50,00"]


for numero, nome, valor in zip(list1, list2, list3):
    print(numero, nome, valor)