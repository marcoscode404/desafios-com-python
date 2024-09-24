from collections import Counter

def contar_palavras(texto):
    palavras = texto.lower().split()
    contagem = Counter(palavras)
    return contagem

texto = input("Digite um texto: ")

contagem = contar_palavras(texto)

for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")