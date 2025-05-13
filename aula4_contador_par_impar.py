# Inicializa os contadores de números pares e ímpares
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para sair): ")

    # Verifica se o usuário deseja finalizar a execução
    if entrada.lower() == 'fim':
        print("Encerrando o programa.")
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1

    except ValueError:
        print("Valor inválido! Informe apenas números inteiros.")

# Exibe a quantidade de números pares e ímpares informados
print("\nResumo final:")
print(f"Total de Pares: {pares}")
print(f"Total de Ímpares: {impares}")
