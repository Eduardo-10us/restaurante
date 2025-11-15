qt = 0
idades = 0

for i in range(3):
    idade = int(input("Informe sua idade: "))

    if idade <= 18:
        qt += 1

    idades += idade

mediaidades = idades / 3

print(f"Quantidade de menores ou iguais a 18 anos = {qt}")
print(f"Média de idades = {mediaidades}")


