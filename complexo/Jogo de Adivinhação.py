#Crie uma classe JogoDeAdivinhacao 
# para gerenciar um jogo onde o jogador deve 
# adivinhar um número aleatório. 
# A classe pode ter métodos para fazer uma tentativa
#  e 
# verificar se o palpite está correto.

import random

class jogo:
    def __init__(self):
        self.numero = random.randint(1, 100)
        self.tentativas = 0

    def tentar_advinhar(self, palpite):
        self.tentativas += 1
        if palpite < self.numero:
            return 'Muito baixo!'
        elif palpite > self.numero:
            return 'Muito Alto!'
        else:
            return f'Parabéns! Você acertou em {self.tentativas}'
        
jogar = jogo()
print(jogar.tentar_advinhar(50))

print(jogar.numero)
    