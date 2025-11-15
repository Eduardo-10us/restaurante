homens = 0
mulheres = 0

for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")

    sexo = input(f"Digite o sexo de {nome} (M/F): ")


    while sexo.lower() not in ["m", "f"]:
        print("Sexo inválido! Digite apenas M ou F.")
        sexo = input(f"Digite o sexo de {nome} (M/F): ")

    if sexo.lower() == "m":
        homens += 1
    else:
        mulheres += 1

print("RESULTADO:")
print(f"Total de homens: {homens}")
print(f"Total de mulheres: {mulheres}")