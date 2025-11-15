homens = 0
mulheres = 0

for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    sexo = input(f"Digite o sexo de {nome} (M/F): ")

    if sexo == "M" or sexo == "m":
        homens += 1
    elif sexo == "F" or sexo == "f":
        mulheres += 1
    else:
        print("Sexo inválido! Contando como 'não informado'.")

print("RESULTADO:")
print(f"Total de homens: {homens}")
print(f"Total de mulheres: {mulheres}")

