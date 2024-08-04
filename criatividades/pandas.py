import pandas as pd

# Carregando os dados
df = pd.read_excel('produtos.xlsx')

# Atualizando preços com um aumento de 10%
df['Preço'] = df['Preço'] * 1.10

# Salvando os dados atualizados
df.to_excel('produtos_atualizados.xlsx', index=False)
