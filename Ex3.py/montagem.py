em_stock = ['processador', 'motherboard', 'memória', 'disco ssd',
            'fonte de alimentação', 'caixa', 'placa gráfica']

pedido = ['caixa', 'processador', 'cooler líquido', 'memória', 'placa gráfica']
essenciais = ['processador', 'motherboard', 'memória']

adicionados = []
em_falta = []

for componente in pedido:
    if componente in em_stock:
        print(f"A adicionar: {componente}")
        adicionados.append(componente)
    else:
        print(f"Sem stock: {componente}")
        em_falta.append(componente)

for essencial in essenciais:
    if essencial not in adicionados:
        print(f"Falta componente essencial: {essencial}\n")

print(f"Componentes adicionados: {sorted(adicionados)}")

if all(essencial in adicionados for essencial in essenciais):
    print("Todos os componentes essenciais foram adicionados.")
else:
    print("Encomenda pendente.")
