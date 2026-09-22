#for numero in range(10, 51, 3):
    #print(numero)

#print (list(range(1, 20)))

#for numero in range(10, 0, -1):
    #print (numero)

Nomes = ["Nathanael", "Lopes", "De" , "Oliveira"]

#for nome in range(0,4):
   # print(Nomes[nome])

#for nome in Nomes:
    #print(f"{nome}", end=" ")

procurada = "Nathanael"
if procurada in Nomes:
    print(f"tem o nome {procurada}")
else:
    print(f"nao tem o nome {procurada}")
print()