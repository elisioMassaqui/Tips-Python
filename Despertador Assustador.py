import winsound
import time

def scary_alarm():
    for frequency in range(100, 1000, 50):  # Frequências de 100 Hz a 1000 Hz
        print(f"Tocando {frequency} Hz")
        winsound.Beep(frequency, 200)  # Duração de 200 milissegundos
        time.sleep(0.1)
    # Sons mais altos e rápidos para o final
    for frequency in range(1000, 3000, 100):
        print(f"Tocando {frequency} Hz")
        winsound.Beep(frequency, 100)  # Duração de 100 milissegundos
        time.sleep(0.05)

if __name__ == '__main__':
    print("Despertador assustador ativado!")
    time.sleep(5)  # Espera 5 segundos antes de iniciar
    scary_alarm()
