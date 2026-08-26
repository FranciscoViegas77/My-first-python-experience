print('hello athlete')
peso = float(input("Introduz o teu peso em kg: "))
altura = float(input("Introduz a tua altura em metros: "))

imc = peso / (altura ** 2)

print(f"\nO teu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Excesso de peso")
else:
    print("Classificação: Obesidade")