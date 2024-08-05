import random
import time

def guess_number():
    print("Bem-vindo ao jogo de adivinhação extrema!")
    
    # Escolher nível de dificuldade
    difficulty = int(input("Escolha o nível de dificuldade (1 - Fácil, 2 - Médio, 3 - Difícil): "))
    
    if difficulty == 1:
        lower_bound = 1
        upper_bound = 50
        max_attempts = 10
    elif difficulty == 2:
        lower_bound = 1
        upper_bound = 100
        max_attempts = 7
    else:
        lower_bound = 1
        upper_bound = 200
        max_attempts = 5
    
    number = random.randint(lower_bound, upper_bound)
    attempts = 0
    start_time = time.time()
    
    while attempts < max_attempts:
        guess = int(input(f"Adivinhe o número ({lower_bound}-{upper_bound}): "))
        attempts += 1
        
        if guess < number:
            print("Muito baixo!")
        elif guess > number:
            print("Muito alto!")
        else:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Parabéns! Você acertou em {attempts} tentativas e {elapsed_time} segundos!")
            break
    else:
        print(f"Você perdeu! O número era {number}.")
        
if __name__ == '__main__':
    guess_number()
