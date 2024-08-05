# Os dicionários são coleções de pares chave-valor.

# Criando um dicionário
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Acessando valores do dicionário
print(person["name"])  # Output: Alice

# Modificando um valor do dicionário
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adicionando um novo par chave-valor
person["email"] = "alice@example.com"
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removendo um par chave-valor
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
