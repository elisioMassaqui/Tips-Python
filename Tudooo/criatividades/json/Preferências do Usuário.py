import json

# Dados JSON para escrever (preferências do usuário)
preferencias_usuario = {
    'tema': 'escuro',
    'notificacoes': True,
    'lingua': 'pt-BR',
    'atalhos': {
        'novo_arquivo': 'Ctrl+N',
        'salvar': 'Ctrl+S',
        'abrir': 'Ctrl+O'
    }
}

# Escrever em um arquivo JSON
with open('preferencias.json', 'w') as file:
    json.dump(preferencias_usuario, file, indent=4)

# Ler de um arquivo JSON
with open('preferencias.json', 'r') as file:
    preferencias_carregadas = json.load(file)
    print(preferencias_carregadas)
