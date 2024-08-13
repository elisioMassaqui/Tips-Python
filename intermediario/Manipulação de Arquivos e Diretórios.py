import os

# Criando diretórios
os.makedirs("Documents/wandi-studio/wandicode", exist_ok=True)

# Escrevendo em um arquivo
caminho = "Documents/wandi-studio/wandicode/wandicode.ino"
with open(caminho, "w", encoding='UTF-8') as arquivo:
    arquivo.write("// Código Arduino\nvoid setup() {}\nvoid loop() {}")

# Lendo de um arquivo
with open(caminho, "r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
