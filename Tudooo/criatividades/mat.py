import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
plt.plot(x, y, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico Simples com Matplotlib')
plt.grid(True)
plt.show()
