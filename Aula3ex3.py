valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra <= 2000:
    desconto = valor_compra * 0.02
elif valor_compra <= 3000:
    desconto = valor_compra * 0.03
elif valor_compra <= 5000:
    desconto = valor_compra * 0.05
else:
    desconto = valor_compra * 0.10

total_pagar = valor_compra - desconto

print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")


