import csv

# Escrever em um arquivo CSV
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Idade'])
    writer.writerow(['Alice', 25])
    writer.writerow(['Bob', 30])

# Ler de um arquivo CSV
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
