alunos = []

def cadastrar():
    resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
    while resp == "S":
        nome = input("Nome do Aluno : ")
        nota = float(input("Nota do Aluno: "))
        alunos.append({"nome":nome, "nota":nota})
        resp = (input("Continuar ? Digite S para sim ou qualquer tecla para não - ")).strip().upper()


def somanotas(alunos):
    qt = 0
    somanota = 0
    for aluno in alunos:
        qt += 1
        nome = aluno["nome"]
        nota = aluno["nota"]
        print(f"Nome do Aluno: {nome} - Nota do Aluno: {nota}")
        somanota += nota

    media = somanota / qt
    return media

cadastrar()
mediaturma = somanotas(alunos)
print(f"A média da turma foi : {mediaturma:.2f}")
