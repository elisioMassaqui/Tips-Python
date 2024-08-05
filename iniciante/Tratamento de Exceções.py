try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except ValueError:
    print("Erro: Valor inválido!")
