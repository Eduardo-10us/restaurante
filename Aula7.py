from pessoa0 import Pessoa


def cadastrar():
    nome=input("Digite Nome:")
    dnasc= input ("Digite data de nascimento")
    sexo= input("Digite sexo:")
    pessoa = Pessoa(nome,dnasc, sexo)
    print("Nome:", pessoa.nome, "Data de nascimento",pessoa.data_nascimento)


resp = "s"


while resp == "s":
    cadastrar()
    resp = input ("deseja continuar?")


