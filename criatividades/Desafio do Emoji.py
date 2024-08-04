import random

emojis = ["🍕", "🚀", "👻", "🎩", "🦄"]
frases = ["Pizza", "Foguete", "Fantasma", "Chapéu", "Unicórnio"]

def desafio_emoji():
    emoji = random.choice(emojis)
    frase = frases[emojis.index(emoji)]
    return emoji, frase

if __name__ == "__main__":
    emoji, frase = desafio_emoji()
    print(f"Emoji: {emoji}")
    resposta = input(f"Qual é a frase para o emoji {emoji}? ")
    if resposta.lower() == frase.lower():
        print("Acertou!")
    else:
        print(f"Errou! A resposta certa era: {frase}")
