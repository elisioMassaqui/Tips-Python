#Herança é foda.
# 1 - Especie
# 2 - Função
# 3 - Tipo na especie
# 4 - Novo Tipo na especie

#Especie
class Animal:
    def __init__(self, nome):
        self.nome =nome
#O que essa especie faz
    def falar(self):
        pass
#Tipo de animal da especie
class Cachorro(Animal):
    def falar(self):
        return 'Au Au!'
#Outro tipo de animal na especie
class Gato(Animal):
    def falar(self):
        return 'Miau!'
#O Rex vai herdar tudo da classe animal
cachorro = Cachorro('Rex')
gato = Gato("Mingau")

print(f'{cachorro.nome} diz: {cachorro.falar()}')
print(f"{gato.nome} diz: {gato.falar()}")