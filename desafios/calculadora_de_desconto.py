def calcular_desconto(preco, desconto):
    valor_final = preco - (preco * (desconto / 100))
    return valor_final

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_final = calcular_desconto(preco, desconto)
print(f"O valor final com desconto é: R${valor_final:.2f}")
print(f"O valor do desconto é: R${preco - valor_final:.2f}")
