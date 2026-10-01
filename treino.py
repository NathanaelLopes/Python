nome = "Alice"
Idade = 25
curso = "Engenharia Informática"

print(f"Nome: {nome}")
print(f"Idade: {Idade}")
print(f"Curso: {curso}\n")

nome2 = "   joao silva   "
print(f"Nome original: {nome2.strip()}")
print(f"Nome original: {nome2.title().strip()}")
print(f"Nome original: {nome2.upper().strip()}")
print(f"Nome original: {nome2.lower().strip()}\n")

print(f"A {nome} tem {Idade} anos\n")

numero1 = 15
numero2 = 4

print(f"Soma: {numero1 + numero2}")
print(f"Subtraçao: {numero1 - numero2}")
print(f"Multiplicaçao: {numero1 * numero2}")
print(f"Divisao: {numero1 / numero2}")

equipamentos = ["computador", "monitor", "impressora"]
equipamentos.append("router")
equipamentos.insert(2, "switch")
equipamentos.remove("monitor")
len(equipamentos)
print(equipamentos)
print("\n")

salas = ["LAB1", "LAB2", "LAB3"]
print(f"Primeira sala: ", salas[0])
print(f"Segunda sala: ", salas[1])
print(f"Terceira sala: ", salas[2])

salas[1] = "LAB2 - Principal"

print("Lista atualizada:", salas)
print("\n")

tipos = ["switch", "computador", "monitor", "impressora", "router"]
print(tipos)
print(f"alfabetica:  {sorted(tipos)}") 
tipos.reverse()
print(f"Reverse:  {tipos}") 