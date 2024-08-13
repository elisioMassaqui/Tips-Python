# Orientada a objectos é foda

# 1 - Especie

# 2 - O que essa especie faz

# 3 - O novo tipo da especie que entrar, vai fazer a mesma coisa, auto

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f'Olá, o meu nome é {self.nome} e tenho {self.idade}'
    
elsio = Pessoa('Elisio', 22)
fania = Pessoa("Fania", 20)
print(elsio.saudacao())
print(fania.saudacao())