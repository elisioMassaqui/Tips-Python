import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Digite o comprimento da senha: "))
    print("Senha gerada:", generate_password(length))
