def chatbot_response(user_input):
    responses = {
        "olá": "Oi! Como posso ajudar você hoje?",
        "qual é o seu nome?": "Eu sou um chatbot criado em Python.",
        "como você está?": "Estou bem, obrigado por perguntar!",
        "tchau": "Até logo! Tenha um ótimo dia!"
    }
    return responses.get(user_input.lower(), "Desculpe, não entendi o que você disse.")

if __name__ == '__main__':
    print("Chatbot ativo! (Digite 'tchau' para sair)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "tchau":
            print("Chatbot: Até logo!")
            break
        print("Chatbot:", chatbot_response(user_input))
