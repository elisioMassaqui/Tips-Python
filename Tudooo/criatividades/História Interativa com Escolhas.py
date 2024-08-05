def inicio():
    print("Você está em uma floresta escura. Há dois caminhos à sua frente.")
    escolha = input("Você vai para a esquerda ou para a direita? (esquerda/direita): ").strip().lower()
    
    if escolha == "esquerda":
        encontro()
    elif escolha == "direita":
        armadilha()
    else:
        print("Escolha inválida. Tente novamente.")
        inicio()

def encontro():
    print("Você encontrou uma cabana estranha.")
    escolha = input("Você entra na cabana ou volta para a floresta? (entrar/voltar): ").strip().lower()

    if escolha == "entrar":
        print("A cabana está vazia, mas você encontra um mapa antigo.")
    elif escolha == "voltar":
        inicio()
    else:
        print("Escolha inválida. Tente novamente.")
        encontro()

def armadilha():
    print("Você caiu em uma armadilha e está preso.")
    escolha = input("Você tenta escapar ou aguarda ajuda? (escapar/aguardar): ").strip().lower()

    if escolha == "escapar":
        print("Você conseguiu escapar da armadilha com sucesso!")
    elif escolha == "aguardar":
        print("Você espera por horas, mas ninguém vem. Eventualmente, você encontra uma saída por conta própria.")
    else:
        print("Escolha inválida. Tente novamente.")
        armadilha()

inicio()
