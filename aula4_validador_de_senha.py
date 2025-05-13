# Programa para verificar se a senha atende aos critérios de segurança: mínimo de 8 caracteres e pelo menos um número

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    # Confere se o usuário optou por finalizar o programa
    if senha.lower() == 'sair':
        print("Programa finalizado.")
        break

    tem_numero = False

    # Percorre cada caractere da senha para checar se há algum número
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break

    # Valida se a senha atende os requisitos de tamanho e presença de número
    if len(senha) < 8:
        print("Senha fraca: ela precisa ter pelo menos 8 caracteres.")
    elif not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
    else:
        print("Senha aprovada com sucesso!")
        break
