import os
import pandas as pd

# Obter o diretório atual
diretorio_atual = os.getcwd()
print(f"Diretório Atual: {diretorio_atual}")

# Listar arquivos em um diretório
arquivos = os.listdir(diretorio_atual)
print(f"Arquivos no diretório atual: {arquivos}")

# Obter variáveis de ambiente
variaveis_ambiente = os.environ
print(f"Variáveis de ambiente: {variaveis_ambiente}")


# Dados para o relatório
data = {
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [28, 22, 34],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

# Criar DataFrame
df = pd.DataFrame(variaveis_ambiente)

# Gerar arquivo CSV
df.to_csv('relatorio.csv', index=False)