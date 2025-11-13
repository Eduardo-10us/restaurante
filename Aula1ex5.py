premio_total = float(input("Digite o valor total do prêmio (em R$): "))

imposto = premio_total * 7/100
premio_liquido = premio_total - imposto

ganhador1 = premio_liquido * 46/100
ganhador2 = premio_liquido * 32/100
ganhador3 = premio_liquido - (ganhador1 + ganhador2)

print(f"Valor total do prêmio = {premio_total:.2f}")
print(f"Desconto do imposto (7%) = {imposto:.2f}")
print(f" Valor Prêmio após imposto = {premio_liquido:.2f}")
print(f" Valor do Ganhador 1 = {ganhador1:.2f}")
print(f"Valor do Ganhador 2 = {ganhador2:.2f}")
print(f"Valor do Ganhador 3 = {ganhador3:.2f}")

