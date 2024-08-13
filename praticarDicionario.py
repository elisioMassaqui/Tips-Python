aluno = {
        "nome": "Carlos",
        "idade": "22",
        "curso": "English", "cor": "mulative"
}

print(aluno['nome'])

aluno['cidade'] = 'São Tomé'
print(aluno)

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")