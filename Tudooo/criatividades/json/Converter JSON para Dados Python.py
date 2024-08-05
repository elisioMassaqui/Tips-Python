import json

# Ler de um arquivo JSON
with open('data.json', 'r') as file:
    data_loaded = json.load(file)

# Converter string JSON para objeto Python
json_str = '{"nome": "Alice", "idade": 25, "cidade": "São Paulo"}'
data_loaded_from_str = json.loads(json_str)
print(json_str)
