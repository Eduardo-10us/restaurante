from pessoa0 import Pessoa

class Aluno (Pessoa):
    def __init__(self,nome,data_nascimento,sexo,matricula):
        super().__init__(nome,data_nascimento,sexo,)
        self.matricula = matricula


aluno1 = Aluno("João silva", "10/01/2005","masculino,20211001")


print(aluno1.nome)
print(aluno1.data_nascimento)
print(aluno1.sexo)
print(aluno1.matricula)


