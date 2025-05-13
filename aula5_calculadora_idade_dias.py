import datetime

# Função que calcula a idade aproximada em dias, com base no ano de nascimento
def calcular_idade_em_dias(ano_nascimento):
    # Captura o ano atual do sistema
    ano_atual = datetime.datetime.now().year

    # Calcula a idade em anos
    idade_anos = ano_atual - ano_nascimento

    # Converte a idade para dias (aproximando por 365 dias por ano)
    idade_dias = idade_anos * 365

    return idade_dias

try:
    # Solicita ao usuário que informe o ano de nascimento
    ano = int(input("Digite o ano de nascimento: "))

    # Valida se o ano informado não está no futuro
    if ano > datetime.datetime.now().year:
        print("Erro: Ano de nascimento no futuro não é permitido.")
    else:
        # Realiza o cálculo da idade em dias e exibe o resultado
        dias = calcular_idade_em_dias(ano)
        print(f"Sua idade aproximada em dias é: {dias} dias.")

except ValueError:
    # Trata o caso em que o usuário não digita um valor numérico válido
    print("Erro: Insira um ano válido.")
