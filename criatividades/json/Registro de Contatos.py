import json

# Dados JSON para escrever (lista de contatos)
contatos = [
    {'nome': 'Carlos', 'telefone': '1234-5678', 'email': 'carlos@example.com'},
    {'nome': 'Maria', 'telefone': '8765-4321', 'email': 'maria@example.com'}
]

# Escrever em um arquivo JSON
with open('contatos.json', 'w') as file:
    json.dump(contatos, file, indent=4)

# Ler de um arquivo JSON
with open('contatos.json', 'r') as file:
    contatos_carregados = json.load(file)
    print(contatos_carregados)
