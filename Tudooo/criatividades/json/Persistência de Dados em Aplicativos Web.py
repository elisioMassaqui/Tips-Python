import json

# Estado do usuário para salvar
user_state = {
    'user_id': 12345,
    'session_id': 'abcde12345',
    'cart': [
        {'product_id': 1, 'quantity': 2, 'price': 100.0},
        {'product_id': 2, 'quantity': 1, 'price': 200.0}
    ],
    'preferences': {
        'currency': 'USD',
        'language': 'en-US'
    }
}

# Escrever estado do usuário em um arquivo JSON
with open('user_state.json', 'w') as file:
    json.dump(user_state, file, indent=4)

# Ler estado do usuário de um arquivo JSON
with open('user_state.json', 'r') as file:
    user_state_loaded = json.load(file)
    print(user_state_loaded)
