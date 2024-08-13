def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero!"
    except TypeError:
        return "Erro: Tipos inválidos!"
    else:
        return resultado
    finally:
        print("Execução da função dividir.")

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "dois"))
