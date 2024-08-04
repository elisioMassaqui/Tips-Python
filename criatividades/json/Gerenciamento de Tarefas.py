import json

# Dados JSON para escrever (lista de tarefas)
tarefas = [
    {'id': 1, 'tarefa': 'Comprar leite', 'concluida': False},
    {'id': 2, 'tarefa': 'Ler um livro', 'concluida': True},
    {'id': 3, 'tarefa': 'Fazer exercício', 'concluida': False}
]

# Escrever em um arquivo JSON
with open('tarefas.json', 'w') as file:
    json.dump(tarefas, file, indent=4)

# Ler de um arquivo JSON
with open('tarefas.json', 'r') as file:
    tarefas_carregadas = json.load(file)
    print(tarefas_carregadas)
