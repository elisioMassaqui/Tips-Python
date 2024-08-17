def function():
    return 29
contatos = [
    {'id': 1, 'name': "Alice", "Telefone": "555"},
    {'id': 2, 'name': "Bob", "Telefone": "59"},
    {'id': 3, 'name': "Julia", "Telefone": "3939"},
    {'id': 4, 'name': "Michael", "Telefone": "2020"},
    {'id': 5, 'name': "Adam", "Telefone": "1020"},
    {'id': 6, 'name': "Peter", "Telefone": "4040"},
    {'id': 7, 'name': "Sally", "Telefone": "02302"},
    {'id': 8, 'name': "Quan", "Telefone": "0102"},
    {"id": 9, 'name': "Leo", "Telefone": "0100"}
]
#for cadaContato in contatos:
#    print(f'{cadaContato['id']} : Nome: {cadaContato['name']} : Telefone: {cadaContato['Telefone']}') 

pesquisarId = int(input('Digite o numero id da pessoa: '))
def pesquisar_contato(id):
    for contacto in contatos:
        if contacto["id"] == id:
            return contacto
print(pesquisar_contato(pesquisarId))