from datetime import datetime, timedelta

# Data e hora atuais
agora = datetime.now()
print(f"Agora: {agora}")

# Formatação de datas
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada: {data_formatada}")

# Operações com datas
ontem = agora - timedelta(days=1)
print(f"Ontem: {ontem}")

# Parsing de datas
data_str = "2023-08-05"
data = datetime.strptime(data_str, "%Y-%m-%d")
print(f"Data convertida: {data}")
