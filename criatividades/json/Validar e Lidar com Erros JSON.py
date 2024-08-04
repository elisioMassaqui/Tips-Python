import json

json_str = '{"nome": "Alice", "idade": 25, "cidade": "São Paulo"'

try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")
