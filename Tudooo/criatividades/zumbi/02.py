import random
import time
import json
import os

# Funções para o jogo
def atacar(arma):
    base_dano = random.randint(1, 10)
    if arma == "espada":
        base_dano += 5
    elif arma == "arco":
        base_dano += 3
    return base_dano

def defender():
    return random.randint(1, 10)

def fugir():
    return random.choice([True, False])

def salvar_progresso(vida_jogador, zumbis, nivel):
    progresso = {
        "vida_jogador": vida_jogador,
        "zumbis": zumbis,
        "nivel": nivel
    }
    with open("progresso.json", "w") as arquivo:
        json.dump(progresso, arquivo)

def carregar_progresso():
    if os.path.exists("progresso.json"):
        with open("progresso.json", "r") as arquivo:
            return json.load(arquivo)
    return None

def jogo():
    progresso = carregar_progresso()
    
    if progresso:
        print("Você tem um progresso salvo. Deseja continuar? (sim/não)")
        continuar = input().strip().lower()
        if continuar == "sim":
            vida_jogador = progresso["vida_jogador"]
            zumbis = progresso["zumbis"]
            nivel = progresso["nivel"]
            print(f"Continuando do nível {nivel} com {vida_jogador} de vida e {zumbis} zumbis restantes.")
        else:
            vida_jogador = 100
            zumbis = 10
            nivel = 1
            print("Iniciando um novo jogo.")
    else:
        vida_jogador = 100
        zumbis = 10
        nivel = 1
        print("Iniciando um novo jogo.")

    armas = ["nada", "espada", "arco"]
    arma = "nada"
    print("Escolha uma arma (nada/espada/arco):")
    escolha_arma = input().strip().lower()
    if escolha_arma in armas:
        arma = escolha_arma

    print("Você está cercado por zumbis! Defenda-se!")

    while zumbis > 0 and vida_jogador > 0:
        acao = input("Escolha uma ação (atacar/defender/fugir/salvar): ").strip().lower()

        if acao == "atacar":
            dano = atacar(arma)
            print(f"Você atacou com a {arma} e causou {dano} de dano!")
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
                salvar_progresso(vida_jogador, zumbis, nivel)
                return
            else:
                print("A tentativa de fuga falhou. Os zumbis atacam!")
                vida_jogador -= 10
                print(f"Sua vida está em {vida_jogador}.")
        elif acao == "salvar":
            salvar_progresso(vida_jogador, zumbis, nivel)
            print("Progresso salvo!")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        time.sleep(1)

    if vida_jogador <= 0:
        print("Você foi derrotado pelos zumbis!")
    else:
        print("Você sobreviveu ao apocalipse zumbi!")
        nivel += 1
        zumbis += 5
        vida_jogador = 100  # Resetando vida para o próximo nível
        salvar_progresso(vida_jogador, zumbis, nivel)
        print(f"Avançando para o nível {nivel}...")

jogo()
