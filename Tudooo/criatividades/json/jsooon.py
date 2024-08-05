import json

# Dados JSON para escrever
data = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo'
}

# Escrever em um arquivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

# Ler de um arquivo JSON
with open('data.json', 'r') as file:
    data_loaded = json.load(file)
    print(data_loaded)
