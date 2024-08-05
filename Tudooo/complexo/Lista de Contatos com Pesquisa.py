contatos = [
    {'id': 1, 'nome': 'Alice', 'telefone': '555'},
    {'id': 2, 'nome': 'Bob', 'telefone': '666'},
    {'id': 3, 'nome': 'Elisio', 'telefone': '930'}
]

pesquisarId = int(input('Digite o numero id da pessoa: '))
def pesquisar_contato(id):
    for contato in contatos:
        if contato['id'] == id:
            return contato
    return None
print(pesquisar_contato(pesquisarId))