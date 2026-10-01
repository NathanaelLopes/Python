notas = [14, 8, 19, 22, 10, 18, -3, 9, 13]

notas_validas = []

for nota in notas:
    if nota < 0 or nota > 20:
        print(f"nota invalida {nota} ")
    elif nota <= 9:
        print(f"insuficiente {nota} ")
        notas_validas.append(nota)
    elif nota <= 13:
        print(f"suficiente {nota} ")
        notas_validas.append(nota)
    elif nota <= 17:
            print(f"bom {nota} ")
            notas_validas.append(nota)
    else:
        print(f"muito bom {nota}")
        notas_validas.append(nota)

print()
print(f"Notas válidas: {len(notas_validas)}")
print(f"Média: {sum(notas_validas) / len(notas_validas)}")
print(f"Nota mais alta: {max(notas_validas)}")
print(f"Nota mais baixa: {min(notas_validas)}")