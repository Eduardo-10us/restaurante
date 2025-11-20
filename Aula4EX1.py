qtd_mulheres = 0
qtd_homens = 0
mulheres_altas = 0
homens_altos = 0
abaixo_160 = 0

resp = "s"

while resp.lower() == "s":
    nome = input("Nome: ")
    sexo = input("Sexo (M/F): ").strip().upper()
    altura = float(input("Altura (ex: 1.70): "))


    if sexo == "F":
        qtd_mulheres += 1
        if altura > 1.65:
            mulheres_altas += 1
    elif sexo == "M":
        qtd_homens += 1
        if altura > 1.70:
            homens_altos += 1


    if altura < 1.60:
        abaixo_160 += 1

    resp = input("Deseja continuar? (S/N): ").strip().upper()


print("\nRESULTADOS:")
print(f"Quantidade de mulheres: {qtd_mulheres}")
print(f"Quantidade de homens: {qtd_homens}")
print(f"Mulheres com altura > 1.65: {mulheres_altas}")
print(f"Homens com altura > 1.70: {homens_altos}")
print(f"Participantes com altura < 1.60: {abaixo_160}")




