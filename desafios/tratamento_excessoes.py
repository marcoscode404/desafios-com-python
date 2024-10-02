a = 2
b = 0

try: 
    print(a/b)
except:  # noqa: E722
    print("Não é permitida divisão por zero")