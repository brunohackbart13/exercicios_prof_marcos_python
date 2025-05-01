preco_produto = float(input(f"Digite o valor do produto para ver o valor final com desconto: ")) #Valor do produto
desconto = 15 #Valor do desconto

valor_final = preco_produto - (preco_produto * desconto / 100) # Formula do desconto
print(f"\n O preço do produto com desconto de {desconto}% é R${valor_final}")