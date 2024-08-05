import json

data = {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

# Converter para string JSON
json_str = json.dumps(data)

# Escrever em um arquivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    print(data)
