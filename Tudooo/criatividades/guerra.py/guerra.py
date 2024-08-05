import random
import time
import json
import os

# Definindo eventos e missões
eventos = [
    "Uma unidade inimiga está se aproximando da sua base!",
    "Você descobre uma nova linha de suprimentos.",
    "O inimigo lançou um ataque aéreo!",
    "Você encontra um aliado que pode oferecer ajuda.",
    "Um espião inimigo foi capturado.",
    "Um grupo de civis está precisando de ajuda.",
    "A base precisa de reparos urgentes!",
    "Você encontrou uma rota de fuga segura.",
    "Uma invasão surpresa está acontecendo!",
    "Você descobre um novo tipo de arma."
]

missao_lista = [
    "Defenda sua base por 3 turnos.",
    "Destrua as unidades inimigas no setor A.",
    "Recupere um item estratégico no setor B.",
    "Negocie um tratado de paz com o inimigo.",
    "Repare as instalações da base.",
    "Recrute uma nova unidade para a sua equipe.",
    "Espione o acampamento inimigo.",
    "Colete informações de inteligência.",
    "Sabote as linhas de suprimento inimigas.",
    "Conclua uma pesquisa de tecnologia."
]

# Funções do jogo
def atacar():
    return random.randint(10, 30)

def defender():
    return random.randint(5, 15)

def negociar():
    return random.choice(["Você conseguiu um tratado de paz temporário!", "A negociação falhou, prepare-se para o ataque!"])

def recrutar():
    return random.choice(["Recrutamento bem-sucedido, nova unidade adicionada!", "Falha no recrutamento, tente novamente."])

def espionar():
    return random.choice(["Informações valiosas obtidas!", "A missão de espionagem falhou."])

def reparar():
    return random.choice(["Reparo bem-sucedido, base mais resistente!", "Falha no reparo, continue tentando."])

def explorar():
    return random.choice(["Você encontrou uma nova rota de fuga.", "Nenhuma novidade encontrada."])

def interagir_aliado():
    return random.choice(["Aliado forneceu suprimentos!", "Aliado não pode ajudar no momento."])

def sabotar():
    return random.choice(["Sabotagem bem-sucedida, inimigos enfraquecidos!", "Sabotagem falhou, inimigos estão alertas."])

def pesquisar():
    return random.choice(["Nova tecnologia descoberta!", "Pesquisa falhou, continue tentando."])

def evento_aleatorio():
    return random.choice(eventos)

def missao(nivel):
    return missao_lista[nivel % len(missao_lista)]

def salvar_progresso(vida_jogador, inimigos, nivel, missao_atual, inventario):
    progresso = {
        "vida_jogador": vida_jogador,
        "inimigos": inimigos,
        "nivel": nivel,
        "missao_atual": missao_atual,
        "inventario": inventario
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
            inimigos = progresso["inimigos"]
            nivel = progresso["nivel"]
            missao_atual = progresso["missao_atual"]
            inventario = progresso["inventario"]
            print(f"Continuando com {vida_jogador} de vida e {inimigos} inimigos restantes.")
        else:
            vida_jogador = 100
            inimigos = 10
            nivel = 1
            missao_atual = missao(nivel)
            inventario = []
            print("Iniciando um novo jogo.")
    else:
        vida_jogador = 100
        inimigos = 10
        nivel = 1
        missao_atual = missao(nivel)
        inventario = []
        print("Iniciando um novo jogo.")

    print(f"Missão atual: {missao_atual}")

    while inimigos > 0 and vida_jogador > 0:
        acao = input("Escolha uma ação (atacar/defender/negociar/recrutar/espionar/reparar/explorar/interagir/sabotar/pesquisar/salvar): ").strip().lower()

        if acao == "atacar":
            dano = atacar()
            print(f"Você atacou e causou {dano} de dano!")
            inimigos -= dano // 10  # Dividido para refletir o número de inimigos restantes
            if inimigos < 0:
                inimigos = 0
            print(f"Restam {inimigos} inimigos.")
        elif acao == "defender":
            bloqueio = defender()
            print(f"Você defendeu e bloqueou {bloqueio} de dano!")
            vida_jogador -= max(0, 20 - bloqueio)
            print(f"Sua vida está em {vida_jogador}.")
        elif acao == "negociar":
            resultado = negociar()
            print(resultado)
            if "falhou" in resultado:
                vida_jogador -= random.randint(10, 30)
                print(f"Sua vida está em {vida_jogador}.")
        elif acao == "recrutar":
            resultado = recrutar()
            print(resultado)
        elif acao == "espionar":
            resultado = espionar()
            print(resultado)
        elif acao == "reparar":
            resultado = reparar()
            print(resultado)
        elif acao == "explorar":
            resultado = explorar()
            print(resultado)
        elif acao == "interagir":
            resultado = interagir_aliado()
            print(resultado)
        elif acao == "sabotar":
            resultado = sabotar()
            print(resultado)
        elif acao == "pesquisar":
            resultado = pesquisar()
            print(resultado)
        elif acao == "salvar":
            salvar_progresso(vida_jogador, inimigos, nivel, missao_atual, inventario)
            print("Progresso salvo!")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        # Verifica se a missão foi cumprida
        if (missao_atual == "Defenda sua base por 3 turnos." and random.randint(1, 3) == 3) or \
           (missao_atual == "Destrua as unidades inimigas no setor A." and inimigos <= 0) or \
           (missao_atual == "Recupere um item estratégico no setor B." and random.choice([True, False])) or \
           (missao_atual == "Negocie um tratado de paz com o inimigo." and random.choice([True, False])) or \
           (missao_atual == "Repare as instalações da base." and random.choice([True, False])) or \
           (missao_atual == "Recrute uma nova unidade para a sua equipe." and random.choice([True, False])) or \
           (missao_atual == "Espione o acampamento inimigo." and random.choice([True, False])) or \
           (missao_atual == "Colete informações de inteligência." and random.choice([True, False])) or \
           (missao_atual == "Sabote as linhas de suprimento inimigas." and random.choice([True, False])) or \
           (missao_atual == "Conclua uma pesquisa de tecnologia." and random.choice([True, False])):
            print("Missão completada!")
            nivel += 1
            missao_atual = missao(nivel)
            inimigos = nivel * 10  # Aumenta o número de inimigos com o nível
            print(f"Avançando para o nível {nivel}... Nova missão: {missao_atual}")

            # Evento aleatório
            print(evento_aleatorio())

        time.sleep(2)

    if vida_jogador <= 0:
        print("Você foi derrotado na batalha!")
    else:
        print("Você venceu a batalha e completou a missão!")

jogo()
