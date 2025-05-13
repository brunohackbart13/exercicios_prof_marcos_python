# Função responsável por calcular o valor da gorjeta
def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# Solicita ao usuário o valor total da conta
total_conta = float(input("Informe o total da conta: "))

# Solicita a porcentagem que será utilizada para calcular a gorjeta
porcentagem = float(input("Informe a porcentagem da gorjeta: "))

# Chama a função para calcular o valor da gorjeta com base nos dados fornecidos
valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)

# Exibe o resultado final para o usuário
print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}")
