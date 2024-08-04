import winsound
import time

def tunnel_effect():
    for _ in range(5):  # Repetir 5 vezes
        for frequency in range(100, 2000, 100):
            print(f"Tocando {frequency} Hz")
            winsound.Beep(frequency, 20)  # Duração curta para efeito de túnel
            time.sleep(0.01)
        for frequency in range(2000, 100, -100):
            print(f"Tocando {frequency} Hz")
            winsound.Beep(frequency, 20)
            time.sleep(0.01)

if __name__ == '__main__':
    print("Efeito túnel de sons iniciado!")
    time.sleep(5)  # Espera 5 segundos antes de iniciar
    tunnel_effect()
