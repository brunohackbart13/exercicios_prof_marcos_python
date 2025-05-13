# Função que verifica se um texto é um palíndromo (lê-se igual de trás para frente)
def validar_palindromo(texto):
    texto_processado = ''

    # Percorre cada caractere, convertendo para minúsculo e mantendo apenas letras e números
    for caractere in texto.lower():
        if caractere.isalnum():  # Checa se é letra ou número
            texto_processado += caractere

    # Compara o texto normal com ele invertido
    return texto_processado == texto_processado[::-1]

# Recebe uma palavra ou frase do usuário
texto = input("Digite uma palavra ou frase: ")

# Chama a função para verificar se é palíndromo
resultado = validar_palindromo(texto)

# Define a resposta a ser exibida de acordo com o resultado
if resultado:
    resposta = "Sim"
else:
    resposta = "Não"

# Mostra o resultado final para o usuário
print(f"'{texto}' é um palíndromo? {resposta}")
