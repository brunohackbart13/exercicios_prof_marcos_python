# Lista para armazenar as notas dos alunos
notas = []
numero_de_alunos = 0

while True:
    entrada = input("Digite a nota do aluno (ou escreva 'fim' para encerrar): ")

    # Verifica se o usuário deseja sair do programa
    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)

        if 0 <= nota <= 10:
            notas.append(nota)
            numero_de_alunos += 1
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    
    except ValueError:
        print("Valor não reconhecido. Informe um número de 0 a 10 ou 'fim'.")

# Faz o cálculo da média e exibe os resultados finais
if numero_de_alunos > 0:
    media = sum(notas) / numero_de_alunos
    print(f"A média da turma é: {media:.2f}")
    print(f"Total de notas registradas: {numero_de_alunos}")
else:
    print("Nenhuma nota foi adicionada.")
