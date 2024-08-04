import json

# Dados JSON para escrever (leituras de sensores)
leituras_sensores = {
    'sensor_temperatura': {'valor': 22.5, 'unidade': 'C'},
    'sensor_umidade': {'valor': 60, 'unidade': '%'},
    'sensor_pressao': {'valor': 1013, 'unidade': 'hPa'}
}

# Escrever em um arquivo JSON
with open('sensores.json', 'w') as file:
    json.dump(leituras_sensores, file, indent=4)

# Ler de um arquivo JSON
with open('sensores.json', 'r') as file:
    sensores_carregados = json.load(file)
    print(sensores_carregados)
