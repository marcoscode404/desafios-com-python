# pip install pandas openpyxl
# pip install XlsxWriter
import pandas as pd

# Dados para o relatório
data = {
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [28, 22, 34],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Gerar arquivo Excel
df.to_excel('relatorio.xlsx', index=False)


# Gerar arquivo Excel com formatação
with pd.ExcelWriter('relatorio_formatado.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Relatório')
    
    # Obter o workbook e worksheet
    workbook = writer.book
    worksheet = writer.sheets['Relatório']
    
    # Ajustar a largura das colunas
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 20)
    
    # Aplicar uma formatação em negrito
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Nome', bold)
    worksheet.write('B1', 'Idade', bold)
    worksheet.write('C1', 'Cidade', bold)


# Gerar múltiplas planilhas no mesmo arquivo Excel
# Você também pode criar várias planilhas dentro de um único arquivo Excel:
with pd.ExcelWriter('relatorio_multiplo.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Dados')
    
    # Criar uma segunda planilha
    summary = pd.DataFrame({
        'Total Pessoas': [df.shape[0]],
        'Idade Média': [df['Idade'].mean()]
    })
    
    summary.to_excel(writer, index=False, sheet_name='Resumo')