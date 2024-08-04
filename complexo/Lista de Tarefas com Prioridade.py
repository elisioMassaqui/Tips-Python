#Crie uma ---lista de tarefas 
# onde cada tarefa é um ---dicionário 
# com informações como descrição e prioridade.
#  Você pode ordenar a lista por prioridade 
# e imprimir as --tarefas mais importantes primeiro.

tarefas = [
    {'tarefa': 'Estudar Python', 'prioridade': 1},
    {'tarefa': 'Fazer exercícios', 'prioridade': 2},
    {'tarefa': 'Ler um livro', 'prioridade': 3}
]
tarefas.sort(key=lambda x: x['prioridade'])
print(tarefas)