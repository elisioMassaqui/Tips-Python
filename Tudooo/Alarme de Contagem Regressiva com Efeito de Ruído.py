import winsound
import time

def countdown_with_noise(seconds):
    for i in range(seconds, 0, -1):
        frequency = 1000 + (seconds - i) * 50  # Aumenta a frequência a cada segundo
        print(f"Tempo restante: {i} segundos")
        winsound.Beep(frequency, 500)
        time.sleep(1)
    print("Tempo esgotado!")
    # Toque final
    winsound.Beep(2000, 1000)  # Som intenso final

if __name__ == '__main__':
    countdown_with_noise(10)  # Contagem regressiva de 10 segundos
