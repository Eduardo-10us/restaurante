salario_bruto= float(input("digite o salario bruto: R$"))
ir= salario_bruto * 0,11
inss= salario_bruto * 0.8
sindicato= salario_bruto * 0.5
total_descontos= ir + inss + sindicato
salario_liquido=salario_bruto - total_descontos
print("salario bruto: R$")

