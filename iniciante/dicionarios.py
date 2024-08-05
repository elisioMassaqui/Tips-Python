# Criando um dicionário
aluno = {
    "nome": "Carlos",
    "idade": 22,
    "curso": "Engenharia"
}

# Acessando valores
print(aluno["nome"])

# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(aluno)

# Iterando sobre um dicionário
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
