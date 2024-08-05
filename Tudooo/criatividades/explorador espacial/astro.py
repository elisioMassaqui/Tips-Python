import random
import time
import json
import os

# Definindo recursos e perigos
recursos = ["minerais", "agua", "energia"]
perigos = ["buraco negro", "tempestade espacial", "alienígenas"]

# Funções do jogo
def explorar():
    evento = random.choice(["recursos", "perigos", "nada"])
    if evento == "recursos":
        recurso = random.choice(recursos)
        print(f"Você encontrou {recurso}!")
        return recurso
    elif evento == "perigos":
        perigo = random.choice(perigos)
        print(f"Cuidado! Você encontrou um {perigo}.")
        return perigo
    else:
        print("Nada de especial encontrado.")
        return None

def coletar_recurso(recurso, inventario):
    if recurso:
        inventario.append(recurso)
        print(f"Recurso {recurso} adicionado ao inventário.")
    else:
        print("Nenhum recurso para coletar.")

def salvar_progresso(vida_jogador, inventario, missao_atual):
    progresso = {
        "vida_jogador": vida_jogador,
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

def missao(nivel):
    missao_lista = [
        "Encontre e colete 3 minerais.",
        "Evite perigos por 5 turnos.",
        "Colete água e energia.",
    ]
    return missao_lista[nivel % len(missao_lista)]

def jogo():
    progresso = carregar_progresso()
    
    if progresso:
        print("Você tem um progresso salvo. Deseja continuar? (sim/não)")
        continuar = input().strip().lower()
        if continuar == "sim":
            vida_jogador = progresso["vida_jogador"]
            inventario = progresso["inventario"]
            missao_atual = progresso["missao_atual"]
            print(f"Continuando com {vida_jogador} de vida.")
        else:
            vida_jogador = 100
            inventario = []
            missao_atual = missao(1)
            print("Iniciando um novo jogo.")
    else:
        vida_jogador = 100
        inventario = []
        missao_atual = missao(1)
        print("Iniciando um novo jogo.")

    nivel = 1

    print(f"Missão atual: {missao_atual}")

    while vida_jogador > 0:
        acao = input("Escolha uma ação (explorar/coletar/salvar): ").strip().lower()

        if acao == "explorar":
            resultado = explorar()
            if resultado in recursos:
                coletar_recurso(resultado, inventario)
            elif resultado in perigos:
                vida_jogador -= random.randint(10, 30)
                print(f"Perigo encontrado! Sua vida está em {vida_jogador}.")
        elif acao == "coletar":
            recurso = input("Qual recurso você deseja coletar? (minerais/agua/energia): ").strip().lower()
            if recurso in recursos:
                coletar_recurso(recurso, inventario)
            else:
                print("Recurso inválido ou não encontrado.")
        elif acao == "salvar":
            salvar_progresso(vida_jogador, inventario, missao_atual)
            print("Progresso salvo!")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        # Verifica se a missão foi cumprida
        if (missao_atual == "Encontre e colete 3 minerais." and inventario.count("minerais") >= 3) or \
           (missao_atual == "Evite perigos por 5 turnos." and random.randint(1, 5) > 4) or \
           (missao_atual == "Colete água e energia." and "agua" in inventario and "energia" in inventario):
            print("Missão completada!")
            nivel += 1
            missao_atual = missao(nivel)
            print(f"Avançando para o nível {nivel}... Nova missão: {missao_atual}")

        time.sleep(1)

    print("Você perdeu todo o oxigênio e foi forçado a abandonar a exploração.")

jogo()
