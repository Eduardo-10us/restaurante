def mostrar_alunos_e_media(turma):
    soma = 0
    print(" Lista de Alunos e Notas ")
    for aluno in turma:
        print(f"Aluno: {aluno['nome']} - Nota: {aluno['nota']}")
        soma += aluno['nota']
    media = soma / len(turma)
    return media


turma = []

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    nota = float(input("Digite a nota do aluno: "))
    turma.append({"nome": nome, "nota": nota})

media = mostrar_alunos_e_media(turma)
print(f"média da turma:{media:2f}")






