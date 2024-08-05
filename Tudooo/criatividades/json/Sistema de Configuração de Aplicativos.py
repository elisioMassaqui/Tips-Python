import json

# Configurações complexas do aplicativo
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'user': 'admin',
        'password': 'senha_secreta'
    },
    'api_keys': {
        'service_1': 'key_service_1',
        'service_2': 'key_service_2'
    },
    'logging': {
        'level': 'DEBUG',
        'file': '/var/log/app.log'
    },
    'features': {
        'feature_x': True,
        'feature_y': False
    }
}

# Escrever configurações em um arquivo JSON
with open('config.json', 'w') as file:
    json.dump(config, file, indent=4)

# Ler configurações de um arquivo JSON
with open('config.json', 'r') as file:
    config_loaded = json.load(file)
    print(config_loaded)
