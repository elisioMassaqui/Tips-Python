import random

def gerar_historia():
    inicios = [
        "Era uma noite sombria e tempestuosa quando",
        "No coração da floresta,",
        "A casa abandonada estava cheia de segredos e",
    ]
    acontecimentos = [
        "algo inexplicável começou a acontecer.",
        "uma presença sinistra foi sentida.",
        "os gritos de um antigo morador ecoaram.",
    ]
    finais = [
        "E ninguém jamais saiu da casa novamente.",
        "Ninguém sabe o que realmente aconteceu naquela noite.",
        "E a lenda continua até hoje.",
    ]

    historia = f"{random.choice(inicios)} {random.choice(acontecimentos)} {random.choice(finais)}"
    return historia

print(gerar_historia())
