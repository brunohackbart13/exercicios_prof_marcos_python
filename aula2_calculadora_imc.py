altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"{imc: .2f} Abaixo do peso")
elif imc <25:
    print(f"{imc: .2f} Peso normal")
elif imc <30:
    print(f"{imc: .2f} Sobrepeso")
else :
    print(f"{imc: .2f} Obesidade")  