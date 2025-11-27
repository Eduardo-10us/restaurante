produtos=[
    {"produto": "TV 50 polegadas", "marca": "samsung"},
    {"produto": "micro-ondas 10 litros", "marca": "Panasonic"},
    {"produto": "iphone 15 pro max", "marca": "Apple"},
    {"produto": "smartphone redmi note 13", "marca": "Xiaomi"},
    {"produto": "lavadora 10 kg", "marca": "Brastemp"}
]

for item in produtos:
    nome = item["produto"]
    marca = item["marca"]
    print(f"Nome={nome}, Marca={marca}")