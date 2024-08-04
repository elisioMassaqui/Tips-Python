import winsound
import time

def siren_effect():
    for _ in range(5):  # Repetir 5 vezes
        for frequency in range(1000, 2000, 50):
            print(f"Tocando {frequency} Hz")
            winsound.Beep(frequency, 50)  # Duração curta para efeito de sirene
            time.sleep(0.01)
        for frequency in range(2000, 1000, -50):
            print(f"Tocando {frequency} Hz")
            winsound.Beep(frequency, 50)
            time.sleep(0.01)

if __name__ == '__main__':
    print("Som de sirene ativado!")
    time.sleep(5)  # Espera 5 segundos antes de iniciar
    siren_effect()
