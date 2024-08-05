import random

def guess_number():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Adivinhe o número (1-100): "))
        if guess < number:
            print("Muito baixo!")
        elif guess > number:
            print("Muito alto!")
        else:
            print("Parabéns! Você acertou!")

if __name__ == '__main__':
    guess_number()
