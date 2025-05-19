my_dicionary = {"A":"AMEIXA", "B": "BOLA", "C": "CACHORRO"}
print(my_dicionary["B"])

for key in my_dicionary:
    print(key+":"+my_dicionary[key])

# CONVERTER DICIONARIO EM TUPLA - (CONJUNTO DE DADOS IMUTAVEIS)
print('----------------------TUPLAS-------------------------')
for i in my_dicionary.items():
    print(i)

# RETORNAR AS CHAVES
print('----------------------KEYS-------------------------')
for i in my_dicionary.keys():
    print(i) 


keys = list(my_dicionary.keys())
print(keys[0])