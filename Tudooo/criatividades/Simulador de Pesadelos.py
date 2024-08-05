import random

def pesadelo():
    cenarios = [
        "Você está em uma casa que parece nunca ter fim.",
        "Você está sendo perseguido por uma sombra que não pode ser vista claramente.",
        "Você está preso em um labirinto que muda constantemente.",
    ]
    efeitos = [
        "O medo se torna insuportável e você acorda em pânico.",
        "Você tenta fugir, mas a sombra está sempre atrás de você.",
        "Você encontra uma saída, mas ela leva a um novo pesadelo.",
    ]
    
    escolha = input("Escolha um pesadelo (1/2/3): ").strip()
    
    if escolha in ["1", "2", "3"]:
        print(f"{random.choice(cenarios)} {random.choice(efeitos)}")
    else:
        print("Escolha inválida. Tente novamente.")
        pesadelo()

pesadelo()
