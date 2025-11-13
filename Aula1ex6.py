paes = int(input("Digite a quantidade de pães vendidos: "))
broas = int(input("Digite a quantidade de broas vendidas: "))

preco_pao = 0.80
preco_broa = 2.50
total_vendas = (paes * preco_pao) + (broas * preco_broa)
custos_fabricacao = total_vendas * 43/100
lucro_liquido = total_vendas - custos_fabricacao

poupanca = lucro_liquido * 15/100
viagem_reais = lucro_liquido * 15/100

cotacao_euro = 6.13
viagem_euros = viagem_reais / cotacao_euro
print(f"Total arrecadado com as vendas= {total_vendas:.2f}")
print(f"Custos de fabricação = {custos_fabricacao:.2f}")
print(f"Lucro líquido= {lucro_liquido:.2f}")
print(f"Valor guardado na poupança = {poupanca:.2f}")
print(f"Valor destinado à viagem = {viagem_reais:.2f}")
print(f"Quantidade de Euros comprados=  {viagem_euros:.2f}")

