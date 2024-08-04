import random
import time
import pygame
import os

# Função para inicializar e carregar sons
def init_sounds():
    pygame.mixer.init()
    sounds = {
        "normal": pygame.mixer.Sound("sounds/normal.wav"),
        "despair": pygame.mixer.Sound("sounds/despair.wav"),
        "hope": pygame.mixer.Sound("sounds/hope.wav")
    }
    return sounds

# Função para tocar um som específico
def play_sound(sound_name, sounds):
    sounds[sound_name].play()

# Função para limpar a tela (cross-platform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_number():
    clear_screen()
    print("Bem-vindo ao Jogo do Medo!")
    time.sleep(1)
    
    # Inicializar sons
    sounds = init_sounds()
    
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
            play_sound("despair", sounds)
        elif guess > number:
            print("Muito alto!")
            play_sound("hope", sounds)
        else:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Parabéns! Você acertou em {attempts} tentativas e {elapsed_time} segundos!")
            play_sound("normal", sounds)
            break
    else:
        clear_screen()
        print("Você perdeu! O número era", number)
        print("Um som arrepiante preenche o ambiente...")
        play_sound("despair", sounds)
        time.sleep(2)
        clear_screen()
        print("Você sente uma presença fria atrás de você...")

if __name__ == '__main__':
    guess_number()
