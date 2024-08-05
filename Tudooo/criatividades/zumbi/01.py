import random
import time

def atacar():
    return random.randint(1, 15)

def defender():
    return random.randint(1, 15)

def fugir():
    return random.choice([True, False])

def jogo():
    zumbis = 10
    vida_jogador = 100
    dificuldade = input("Escolha a dificuldade (fácil/médio/difícil): ").strip().lower()

    if dificuldade == "fácil":
        zumbis = 5
    elif dificuldade == "médio":
        zumbis = 10
    elif dificuldade == "difícil":
        zumbis = 15
    else:
        print("Dificuldade inválida. Usando a dificuldade média.")
        zumbis = 10

    print("Você está cercado por zumbis! Defenda-se!")

    while zumbis > 0 and vida_jogador > 0:
        acao = input("Escolha uma ação (atacar/defender/fugir): ").strip().lower()

        if acao == "atacar":
            dano = atacar()
            print(f"Você atacou e causou {dano} de dano!")
            zumbis -= dano
            if zumbis < 0:
                zumbis = 0
            print(f"Restam {zumbis} zumbis.")
        elif acao == "defender":
            bloqueio = defender()
            print(f"Você defendeu e bloqueou {bloqueio} de dano!")
            vida_jogador -= max(0, 10 - bloqueio)
            print(f"Sua vida está em {vida_jogador}.")
        elif acao == "fugir":
            if fugir():
                print("Você conseguiu fugir com sucesso!")
                return
            else:
                print("A tentativa de fuga falhou. Os zumbis atacam!")
                vida_jogador -= 10
                print(f"Sua vida está em {vida_jogador}.")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        time.sleep(1)

    if vida_jogador <= 0:
        print("Você foi derrotado pelos zumbis!")
    else:
        print("Você sobreviveu ao apocalipse zumbi!")

jogo()
