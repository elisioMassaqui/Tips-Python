import random
import time

def atacar():
    return random.randint(1, 10)

def defender():
    return random.randint(1, 10)

def jogo():
    zumbis = 10
    vida_jogador = 100

    print("Você está cercado por zumbis! Defenda-se!")

    while zumbis > 0 and vida_jogador > 0:
        acao = input("Escolha uma ação (atacar/defender): ").strip().lower()

        if acao == "atacar":
            dano = atacar()
            print(f"Você atacou e causou {dano} de dano!")
            zumbis -= dano
            print(f"Restam {zumbis} zumbis.")
        elif acao == "defender":
            bloqueio = defender()
            print(f"Você defendeu e bloqueou {bloqueio} de dano!")
            vida_jogador -= max(0, 10 - bloqueio)
            print(f"Sua vida está em {vida_jogador}.")
        else:
            print("Ação inválida.")

        time.sleep(1)

    if vida_jogador <= 0:
        print("Você foi derrotado pelos zumbis!")
    else:
        print("Você sobreviveu ao apocalipse zumbi!")

jogo()
