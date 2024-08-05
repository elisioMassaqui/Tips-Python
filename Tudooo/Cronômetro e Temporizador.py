import time

def stopwatch():
    start_time = time.time()
    input("Pressione Enter para parar o cronômetro...")
    elapsed_time = time.time() - start_time
    print(f"Tempo decorrido: {elapsed_time:.2f} segundos")


def timer(seconds):
    print(f"Temporizador de {seconds} segundos iniciado...")
    time.sleep(seconds)
    print("Tempo esgotado!")

if __name__ == '__main__':
    choice = input("Digite 'stopwatch' para o cronômetro ou 'timer' para o temporizador: ").strip().lower()
    if choice == 'stopwatch':
        stopwatch()
    elif choice == 'timer':
        seconds = int(input("Quantos segundos? "))
        timer(seconds)
    else:
        print("Escolha inválida.")
