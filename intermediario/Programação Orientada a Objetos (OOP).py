class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos'
    
pessoa1 = Pessoa('Elisio', 22)
pessoa2 = Pessoa('Fânia', 20)
print(pessoa1.saudacao())
print(pessoa2.saudacao())