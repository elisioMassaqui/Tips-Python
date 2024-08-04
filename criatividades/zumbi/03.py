import random
import time
import json
import os

# Definindo tipos de zumbis
zumbis_types = {
    "zumbi_comum": {"vida": 20, "dano": 5},
    "zumbi_forte": {"vida": 40, "dano": 10},
    "zumbi_rápido": {"vida": 15, "dano": 7}
}

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

def salvar_progresso(vida_jogador, zumbis, nivel, inventario, missao_atual):
    progresso = {
        "vida_jogador": vida_jogador,
        "zumbis": zumbis,
        "nivel": nivel,
        "inventario": inventario,
        "missao_atual": missao_atual
    }
    with open("progresso.json", "w") as arquivo:
        json.dump(progresso, arquivo)

def carregar_progresso():
    if os.path.exists("progresso.json"):
        with open("progresso.json", "r") as arquivo:
            return json.load(arquivo)
    return None

def gerar_zumbis(nivel):
    tipo = random.choice(list(zumbis_types.keys()))
    vida = zumbis_types[tipo]["vida"] + (nivel * 5)
    dano = zumbis_types[tipo]["dano"]
    return {"tipo": tipo, "vida": vida, "dano": dano}

def missao(nivel):
    missao_lista = [
        "Sobreviva a uma horda de zumbis.",
        "Encontre e colete um item especial.",
        "Defenda uma posição por um tempo.",
    ]
    return missao_lista[nivel % len(missao_lista)]

def jogo():
    progresso = carregar_progresso()
    
    if progresso:
        print("Você tem um progresso salvo. Deseja continuar? (sim/não)")
        continuar = input().strip().lower()
        if continuar == "sim":
            vida_jogador = progresso["vida_jogador"]
            zumbis = progresso["zumbis"]
            nivel = progresso["nivel"]
            inventario = progresso["inventario"]
            missao_atual = progresso["missao_atual"]
            print(f"Continuando do nível {nivel} com {vida_jogador} de vida e {zumbis} zumbis restantes.")
        else:
            vida_jogador = 100
            nivel = 1
            inventario = []
            missao_atual = missao(nivel)
            print("Iniciando um novo jogo.")
            zumbis = gerar_zumbis(nivel)
    else:
        vida_jogador = 100
        nivel = 1
        inventario = []
        missao_atual = missao(nivel)
        print("Iniciando um novo jogo.")
        zumbis = gerar_zumbis(nivel)

    armas = ["nada", "espada", "arco"]
    arma = "nada"
    print("Escolha uma arma (nada/espada/arco):")
    escolha_arma = input().strip().lower()
    if escolha_arma in armas:
        arma = escolha_arma

    print(f"Missão atual: {missao_atual}")

    while zumbis["vida"] > 0 and vida_jogador > 0:
        acao = input("Escolha uma ação (atacar/defender/fugir/salvar): ").strip().lower()

        if acao == "atacar":
            dano = atacar(arma)
            print(f"Você atacou com a {arma} e causou {dano} de dano!")
            zumbis["vida"] -= dano
            if zumbis["vida"] < 0:
                zumbis["vida"] = 0
            print(f"O zumbi restante tem {zumbis['vida']} de vida.")
        elif acao == "defender":
            bloqueio = defender()
            print(f"Você defendeu e bloqueou {bloqueio} de dano!")
            vida_jogador -= max(0, zumbis["dano"] - bloqueio)
            print(f"Sua vida está em {vida_jogador}.")
        elif acao == "fugir":
            if fugir():
                print("Você conseguiu fugir com sucesso!")
                salvar_progresso(vida_jogador, zumbis, nivel, inventario, missao_atual)
                return
            else:
                print("A tentativa de fuga falhou. O zumbi atacou!")
                vida_jogador -= zumbis["dano"]
                print(f"Sua vida está em {vida_jogador}.")
        elif acao == "salvar":
            salvar_progresso(vida_jogador, zumbis, nivel, inventario, missao_atual)
            print("Progresso salvo!")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        if zumbis["vida"] <= 0:
            print("Você derrotou o zumbi!")
            nivel += 1
            zumbis = gerar_zumbis(nivel)
            inventario.append("item especial")
            missao_atual = missao(nivel)
            print(f"Avançando para o nível {nivel}... Nova missão: {missao_atual}")

        time.sleep(1)

    if vida_jogador <= 0:
        print("Você foi derrotado pelos zumbis!")
    else:
        print("Você sobreviveu ao apocalipse zumbi!")

jogo()
