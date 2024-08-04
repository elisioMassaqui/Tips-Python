import random

def generate_random_text(words, length=50):
    text = []
    for _ in range(length):
        word = random.choice(words)
        text.append(word)
    return ' '.join(text)

if __name__ == '__main__':
    words = ["o", "rápido", "marrom", "urso", "pular", "sobre", "o", "cachorro", "preguiçoso"]
    print("Texto gerado:", generate_random_text(words))
