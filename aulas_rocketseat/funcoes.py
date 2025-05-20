# EXEMPLOS
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Bob")




# FUNÇÃO COM RETORNO
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando função quadrado: ")
resultado_quadrado = quadrado(10)
print("\n Resultado da função quadrado:", resultado_quadrado)


#CHAMANDO FUNÇÃO COM MULTIPLOS PARAMETROS
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n Chamando a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s" % (numero1, numero2, resultado_soma))