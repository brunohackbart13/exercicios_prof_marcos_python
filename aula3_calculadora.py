while True:
    try:
        # Entrada de números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Escolha da operação
        operacao = input("Digite a operação (+ , - , * , / ): ")

        # Execução conforme a operação escolhida
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Coleguinha, você não pode dividir por zero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação Inválida.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as e:
        if str(e) == "Operação Inválida.":
            print(e)
        else:
            print("Entrada inválida, digite novamente.")

    except ZeroDivisionError as e:
        print(e)
