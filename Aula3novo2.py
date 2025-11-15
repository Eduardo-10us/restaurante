media_escola=7,0
qtd_alunos=int(input("Quantos alunos tem na turma ?"))
soma_medias=0
for i in range(qtd_alunos):
    print(f"\n aluno {i +1}")
    nome=input("nome do aluno:")

    n1=float(input("nota 1:"))
    n2 = float(input("nota 2:"))


    media=(n1+n2) / 2
    soma_medias += media
    print(f"Média anual de (nome):{media:.2f}")

    if media_escola >= 7:
        print("situação Aprovado")
    else:
        print("situação Reprovado")

    media_turma = soma_medias / qtd_alunos
    print(f"\nmédia da turma: {media_turma:.2f}")

