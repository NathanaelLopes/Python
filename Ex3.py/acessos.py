autorizados = ['Ana', 'RUI', 'marta', 'Tiago', 'admin']
tentativas = [' rui', 'Joana ', 'ADMIN', 'Marta', 'pedro']

autorizados_min = []
negados = []

for nome in autorizados:
    autorizados_min.append(nome.lower())

for nome in tentativas:

    nome = nome.strip().lower()

    if nome not in autorizados_min:
        print(f'Acesso negado: {nome.title()}')
        negados.append(nome)

    elif nome == 'admin':
        print('Bem-vindo, administrador! Queres ver o registo de acessos?')

    else:
        print(f'Acesso autorizado: {nome.title()}')

if negados:
    print(f'Acessos negados: {len(negados)}')
else:
    print('Nenhum acesso negado.')


