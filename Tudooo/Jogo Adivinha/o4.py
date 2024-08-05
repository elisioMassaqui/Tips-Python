import random
import winsound
import time
import threading

# Função para tocar o alarme assustador continuamente
def scary_alarm():
    while True:
        for frequency in range(100, 1000, 50):  # Frequências de 100 Hz a 1000 Hz
            winsound.Beep(frequency, 200)  # Duração de 200 milissegundos
            time.sleep(0.1)
        # Sons mais altos e rápidos para o final
        for frequency in range(1000, 3000, 100):
            winsound.Beep(frequency, 100)  # Duração de 100 milissegundos
            time.sleep(0.05)

# Função para tocar um beep contínuo com uma frequência específica
def beep_continuous(frequency, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        winsound.Beep(frequency, 500)  # Toca um beep com a frequência especificada e duração de 500 ms
        time.sleep(0.1)  # Pequena pausa entre beeps para evitar sobreposição

def guess_number():
    number = random.randint(1, 100)
    guess = None
    
    # Iniciar o alarme assustador em um thread separado
    print("Iniciando alarme assustador...")
    alarm_thread = threading.Thread(target=scary_alarm, daemon=True)
    alarm_thread.start()
    
    while guess != number:
        guess = int(input("Adivinhe o número (1-100): "))
        if guess < number:
            print("Muito baixo! Alterando som para desespero...")
            beep_continuous(400, 1)  # Frequência baixa por 1 segundo
        elif guess > number:
            print("Muito alto! Alterando som para esperança...")
            beep_continuous(600, 1)  # Frequência média por 1 segundo
        else:
            print("Parabéns! Você acertou!")
            beep_continuous(800, 1)  # Frequência alta por 1 segundo
            break  # Encerrar o loop após acerto

    # Opcional: Encerrar o alarme assustador após o jogo
    print("Encerrando alarme assustador...")
    # Interromper o alarme (não implementado aqui, a thread está configurada como daemon e terminará ao encerrar o script)

if __name__ == '__main__':
    guess_number()
