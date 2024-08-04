def auto_reply(message):
    return f"Você disse: {message}. Eu sou um bot!"

if __name__ == '__main__':
    message = input("Digite sua mensagem: ")
    print(auto_reply(message))
