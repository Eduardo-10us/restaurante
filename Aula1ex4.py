import math
altura=float(input("digite a altura da parede (m):"))
comprimento=float(input("digite o comprimento da parede (m):"))
area=altura*comprimento
litros=area/3
latas=litros/3.6
latas=math.ceil(litros/3.6)
preco_total=latas*107
print(" area total: ",area,"metros")
print("quantidade de tinta necessaria",litros,"litros")
print("quantidade de latas necessarias:",latas,"latas")
print(f"Valor a ser gasto: R${preco_total:2f}")


