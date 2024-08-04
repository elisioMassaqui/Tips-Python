import scheduleeee
import time

def tarefa():
    print("Tarefa executada!")

# Agendar a tarefa para executar a cada minuto
scheduleeee.every(1).minutes.do(tarefa)

while True:
    scheduleeee.run_pending()
    time.sleep(1)
