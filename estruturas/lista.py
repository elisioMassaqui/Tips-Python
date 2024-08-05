# Criando uma lista
fruits = ["apple", "banana", "cherry"]

# Acessando elementos da lista
print(fruits[0])  # Output: apple

# Modificando um elemento da lista
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adicionando um elemento à lista
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removendo um elemento da lista
fruits.remove("apple")
print(fruits)  # Output: ['blueberry', 'cherry', 'orange']
