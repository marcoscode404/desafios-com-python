import os

# Obter o diretório atual
diretorio_atual = os.getcwd()
print(f"Diretório Atual: {diretorio_atual}")

# Listar arquivos em um diretório
arquivos = os.listdir(diretorio_atual)
print(f"Arquivos no diretório atual: {arquivos}")

# Obter variáveis de ambiente
variaveis_ambiente = os.environ
print(f"Variáveis de ambiente: {variaveis_ambiente}")
