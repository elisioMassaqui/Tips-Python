import winsound
import time
import random

def random_noise():
    for _ in range(10):  # Toca 10 sons aleatórios
        frequency = random.randint(100, 3000)
        duration = random.randint(100, 1000)
        print(f"Tocando {frequency} Hz por {duration} milissegundos")
        winsound.Beep(frequency, duration)
        time.sleep(random.uniform(0.1, 1.0))  # Pausa aleatória

if __name__ == '__main__':
    print("Ruído aleatório iniciado!")
    time.sleep(5)  # Espera 5 segundos antes de iniciar
    random_noise()
