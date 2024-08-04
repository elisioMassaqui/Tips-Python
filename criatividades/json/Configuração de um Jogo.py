import json

# Dados JSON para escrever (configurações do jogo)
configuracao_jogo = {
    'resolucao': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controles': {
        'mover_para_frente': 'W',
        'mover_para_tras': 'S',
        'mover_para_esquerda': 'A',
        'mover_para_direita': 'D'
    }
}

# Escrever em um arquivo JSON
with open('config_jogo.json', 'w') as file:
    json.dump(configuracao_jogo, file, indent=4)

# Ler de um arquivo JSON
with open('config_jogo.json', 'r') as file:
    configuracao_carregada = json.load(file)
    print(configuracao_carregada)
