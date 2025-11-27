pessoas= [
    {"nome":"joao","idade":30},
    {"nome":"Maria","idade":20}
]

for pessoa in pessoas:
    nome=pessoa["nome"]
    idade=pessoa["idade"]
    print(f"Nome={nome},Idade={idade}")

