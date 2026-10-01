# R0 - Menu principal

# Constantes (tuplas)
SALAS = ('LAB1', 'LAB2', 'LAB3')
ESTADOS = ('operacional', 'avariado', 'em reparação')

# Lista de tipos de equipamento aceites
tipos = ['computador', 'monitor', 'impressora', 'router', 'switch', 'projetor']

# Inventário pré-carregado (dicionário de dicionários)
inventario = {
    'PC01': {'nome': 'desktop hp elitedesk',
            'tipo': 'computador',
            'sala': 'LAB1',
            'quantidade': 12,
            'estado': 'operacional'},

    'PC02': {'nome': 'portátil lenovo thinkpad',
            'tipo': 'computador',
            'sala': 'LAB2', 
            'quantidade': 8, 
            'estado': 'avariado'},

    'MON01': {'nome': 'monitor dell 24 polegadas',
             'tipo': 'monitor',
              'sala': 'LAB1', 
              'quantidade': 12, 
              'estado': 'operacional'},

    'IMP01': {'nome': 'impressora epson laser', 
              'tipo': 'impressora',
              'sala': 'LAB3', 
              'quantidade': 2, 
              'estado': 'avariado'},

    'RT01': {'nome': 'router cisco', 
             'tipo': 'router',
             'sala': 'LAB2', 
             'quantidade': 1, 
             'estado': 'em reparação'},

    'PRJ01': {'nome': 'projetor benq', 
              'tipo': 'projetor',
              'sala': 'LAB3', 
              'quantidade': 1, 
              'estado': 'operacional'},
}

# lista_reparacao construída automaticamente a partir do inventário
lista_reparacao = []
for codigo, dados in inventario.items():
    if dados['estado'] == 'avariado':
        lista_reparacao.append(codigo)

reparados = []
historico = []

# Texto do menu construído linha a linha com +=
menu = ""
menu += "\n========== INVENTÁRIO DO LABORATÓRIO ==========\n"
menu += "1 - Opção 1\n"
menu += "2 - Opção 2\n"
menu += "3 - Opção 3\n"
menu += "4 - Opção 4\n"
menu += "5 - Opção 5\n"
menu += "6 - Opção 6\n"
menu += "7 - Opção 7\n"
menu += "8 - Opção 8\n"
menu += "0 - Sair\n"
menu += "===============================================\n"
menu += "Escolha uma opção: "

# Ciclo principal controlado por uma flag
ativo = True
while ativo:
    opcao = int(input(menu))

    if opcao == 1:
        print("A executar a opção 1...")
    elif opcao == 2:
        print("A executar a opção 2...")
    elif opcao == 3:
        print("A executar a opção 3...")
    elif opcao == 4:
        print("A executar a opção 4...")
    elif opcao == 5:
        print("A executar a opção 5...")
    elif opcao == 6:
        print("A executar a opção 6...")
    elif opcao == 7:
        print("A executar a opção 7...")
    elif opcao == 8:
        print("A executar a opção 8...")
    elif opcao == 0:
        # Confirmação antes de sair
        resposta = input("Tem a certeza que deseja sair? (s/n): ").strip().lower()
        if resposta == 's':
            ativo = False
            print("A sair do programa. Até breve!")
    else:
        print("Opção inexistente. Escolha um número de 0 a 8.")