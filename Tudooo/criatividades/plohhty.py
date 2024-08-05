import plotly.express as px

# Dados para o gráfico
data = {
    'Ano': [2020, 2021, 2022],
    'Vendas': [100, 150, 200]
}

# Criar o gráfico
fig = px.line(data, x='Ano', y='Vendas', title='Vendas ao Longo dos Anos')
fig.show()
