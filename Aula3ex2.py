nivel = int(input("Digite o nível do professor (1 ou 2): "))
horas = float(input("Digite a quantidade de horas/aula dadas no mês: "))

if nivel == 1:
    valor_hora = 56
elif nivel == 2:
    valor_hora = 66
else:
    print("Nível inválido! Digite 1 ou 2.")
    exit()
salario_base = valor_hora * horas
dsr = salario_base * 0.15
salario_total = salario_base + dsr
print(f"Salário base: R${salario_base:.2f}")
print(f"DSR (15%): R${dsr:.2f}")
print(f"Salário total: R${salario_total:.2f}")