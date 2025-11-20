total_pacientes = 0
total_pediatria = 0
total_clinica = 0

resp = input("Entrar no cadastro do dia? Digite S para sim ou qualquer tecla para não: ").strip().upper()

while resp == "S":
    nome = input("Nome do paciente: ")
    idade = input("Idade do paciente: ")
    medico = input("Nome do médico: ")
    especialidade = input("Especialidade P = Pediatria - C = Clínica médica: ").strip().upper()

    if especialidade == "P":
        total_pediatria += 1
    elif especialidade == "C":
        total_clinica += 1
    else:
        print("Especialidade inválida")
        continue

    total_pacientes += 1

    resp = input("Continuar no cadastro? Digite S para sim ou qualquer tecla para não: ").strip().upper()

print(f"Quantidade total de pacientes: {total_pacientes}")
print(f"Quantidade de pacientes na Clínica Médica: {total_clinica}")
print(f"Quantidade de pacientes na Pediatria: {total_pediatria}")





