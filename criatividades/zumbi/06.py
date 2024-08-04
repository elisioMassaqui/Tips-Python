import random
import time

class Zumbi:
    def __init__(self, tipo, vida):
        self.tipo = tipo
        self.vida = vida

    def atacar(self):
        dano = random.randint(1, 10)
        return dano

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def __str__(self):
        return f"{self.tipo} com {self.vida} de vida"

def habilidades_jogador():
    habilidades = {
        'Golpe Mortal': lambda: random.randint(15, 25),
        'Ataque Rápido': lambda: random.randint(5, 10),
        'Arremesso Explosivo': lambda: random.randint(10, 20) * 2
    }
    return habilidades

def escolher_acao():
    print("\nEscolha sua ação:")
    print("1. Atacar")
    print("2. Defender")
    print("3. Usar habilidade especial")
    escolha = input("Digite o número da sua escolha: ").strip()
    return escolha

def jogo():
    tipos_zumbis = [
        ('Zumbi Básico', 30),
        ('Zumbi Forte', 50),
        ('Zumbi Rápido', 20),
        ('Zumbi Gigante', 100)
    ]
    zumbis = [Zumbi(tipo, vida) for tipo, vida in tipos_zumbis]
    vida_jogador = 100
    habilidades = habilidades_jogador()

    print("Você está cercado por zumbis! Prepare-se para a batalha!")

    while zumbis and vida_jogador > 0:
        print("\nZumbis restantes:")
        for i, zumbi in enumerate(zumbis):
            print(f"{i + 1}. {zumbi}")

        acao = escolher_acao()

        if acao == "1":
            zumbi = random.choice(zumbis)
            dano = random.randint(5, 15)
            print(f"\nVocê atacou o {zumbi.tipo} e causou {dano} de dano!")
            zumbi.receber_dano(dano)
            if zumbi.vida == 0:
                zumbis.remove(zumbi)
                print(f"O {zumbi.tipo} foi derrotado!")
            else:
                print(f"O {zumbi.tipo} agora tem {zumbi.vida} de vida.")
        elif acao == "2":
            bloqueio = random.randint(5, 15)
            print(f"\nVocê usou um bloqueio e bloqueou {bloqueio} de dano!")
            dano_recebido = sum(zumbi.atacar() for zumbi in zumbis) - bloqueio
            vida_jogador -= max(0, dano_recebido)
            print(f"Sua vida está em {vida_jogador}.")
        elif acao == "3":
            print("\nEscolha uma habilidade especial:")
            for i, habilidade in enumerate(habilidades.keys()):
                print(f"{i + 1}. {habilidade}")
            escolha_habilidade = input("Digite o número da habilidade: ").strip()
            if escolha_habilidade in ["1", "2", "3"]:
                habilidade = list(habilidades.keys())[int(escolha_habilidade) - 1]
                dano = habilidades[habilidade]()
                print(f"\nVocê usou {habilidade} e causou {dano} de dano!")
                if zumbis:
                    zumbi = random.choice(zumbis)
                    zumbi.receber_dano(dano)
                    if zumbi.vida == 0:
                        zumbis.remove(zumbi)
                        print(f"O {zumbi.tipo} foi derrotado!")
                    else:
                        print(f"O {zumbi.tipo} agora tem {zumbi.vida} de vida.")
                else:
                    print("Não há zumbis restantes para atacar!")
            else:
                print("Escolha de habilidade inválida.")
        else:
            print("Ação inválida. Tente novamente.")

        if zumbis:
            for zumbi in zumbis:
                dano_zumbi = zumbi.atacar()
                vida_jogador -= dano_zumbi
                print(f"\nO {zumbi.tipo} atacou e causou {dano_zumbi} de dano!")
                if vida_jogador <= 0:
                    vida_jogador = 0
                    break
            print(f"Sua vida agora está em {vida_jogador}.")

        time.sleep(1)

    if vida_jogador <= 0:
        print("\nVocê foi derrotado pelos zumbis! O apocalipse zumbi venceu.")
    else:
        print("\nVocê sobreviveu ao apocalipse zumbi e derrotou todos os inimigos!")

jogo()
