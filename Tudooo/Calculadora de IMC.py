def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Abaixo do peso"
    elif 18.5 <= bmi < 24.9:
        category = "Peso normal"
    elif 25 <= bmi < 29.9:
        category = "Sobrepeso"
    else:
        category = "Obesidade"
    return bmi, category

if __name__ == '__main__':
    weight = float(input("Digite seu peso (kg): "))
    height = float(input("Digite sua altura (m): "))
    bmi, category = calculate_bmi(weight, height)
    print(f"Seu IMC é {bmi:.2f}, o que indica: {category}")
