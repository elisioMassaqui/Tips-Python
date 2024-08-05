import schedule
import time

def tarefa():
    print("Tarefa executada!")

# Agendar a tarefa para executar a cada minuto
schedule.every(1).seconds.do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
