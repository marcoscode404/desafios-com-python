print("Exemplo de captura de excções")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro de value error: {e}")
        raise ValueError("Tipo de variaveis incompativeis")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação finalizada")