import winsound
import time

def test_hearing():
    for frequency in range(100, 2000, 100):  # Frequências de 100 Hz a 2000 Hz
        print(f"Tocando {frequency} Hz")
        winsound.Beep(frequency, 500)  # Duração de 500 milissegundos
        time.sleep(0.5)

if __name__ == '__main__':
    test_hearing()
