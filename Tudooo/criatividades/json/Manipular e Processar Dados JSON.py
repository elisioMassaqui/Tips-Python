import json

# Ler de um arquivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Acessar dados
nome = data['nome']
idade = data['idade']

# Modificar dados
data['cidade'] = 'Rio de Janeiro'

# Salvar alterações de volta no arquivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    print(data)
