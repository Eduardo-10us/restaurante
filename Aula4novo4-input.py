produtos = []

resp = (input("Entrar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()
while resp == "S":
    produto = input("Digite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    produtos.append({"produto":produto, "marca": marca})
    resp = (input("continuar no Cadastro? Digite S para sim ou qualquer tecla para não - ")).strip().upper()

for prod in produtos:
    produto = prod["produto"]
    marca = prod["marca"]
    print(f"Produto = {produto} - Marca = {marca}")
