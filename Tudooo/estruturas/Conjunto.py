# Os conjuntos são coleções não ordenadas de itens únicos.

# Criando um conjunto
colors = {"red", "green", "blue"}

# Adicionando um elemento ao conjunto
colors.add("yellow")
print(colors)  # Output: {'blue', 'green', 'yellow', 'red'}

# Removendo um elemento do conjunto
colors.remove("green")
print(colors)  # Output: {'blue', 'yellow', 'red'}

# Verificando se um elemento está no conjunto
print("red" in colors)  # Output: True
