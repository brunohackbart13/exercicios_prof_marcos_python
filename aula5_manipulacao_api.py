import requests

url = "https://randomuser.me/api"

# Envia uma requisição GET para a URL informada
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Obtém os dados do primeiro usuário retornado pela API
    user = data['results'][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user['location']['country']

    # Exibe as informações extraídas do usuário
    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"País: {country}")

else:
    # Caso a API retorne erro, exibe o status code recebido
    print(f"Erro ao acessar a API: {response.status_code}")
