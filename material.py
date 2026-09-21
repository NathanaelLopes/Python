material = []

material.append("computador")
material.append("cabo hdmi")
material.append("rato")

print(material)

material.insert(0, "projetor")

print(material)

material[3] = "teclado"

print(material)

material.insert(2, "extensao eletrica")

print(material)

ja_existe = material.pop(1)  

print(f"O material {ja_existe} já existe na sala")
print(material)

del material [0]

print(material)