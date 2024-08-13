class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

cachorro = Cachorro("Rex")
gato = Gato("Mingau")

print(f"{cachorro.nome} diz: {cachorro.falar()}")
print(f"{gato.nome} diz: {gato.falar()}")
