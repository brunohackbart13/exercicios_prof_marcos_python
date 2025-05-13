# Função que calcula o valor da gorjeta com base no valor da conta e na porcentagem informada
def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# Função que soma o valor da conta com a gorjeta para obter o total a pagar
def valor_total(valor_conta, valor_gorjeta):
    total = valor_conta + valor_gorjeta
    return total

# Recebe do usuário o valor total da conta
total_conta = float(input("Informe o total da conta: "))

# Recebe a porcentagem da gorjeta desejada
porcentagem = float(input("Informe a porcentagem da gorjeta: "))

# Calcula o valor da gorjeta chamando a função apropriada
valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)

# Calcula o valor total a ser pago (conta + gorjeta)
total_a_pagar = valor_total(total_conta, valor_gorjeta)

# Exibe o valor da gorjeta calculada
print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}")

# Mostra o valor final a ser pago, já com a gorjeta incluída
print(f"O valor total da conta (conta + gorjeta) é: R${total_a_pagar:.2f}")
