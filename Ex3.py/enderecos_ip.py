enderecos = [(192, 168, 1, 20), (10, 0, 0, 1), (8, 8, 8, 8), (172, 20, 3, 4), (172, 32, 1, 1), (127, 0, 0, 1), (224, 0, 0, 9)]

for endereco in enderecos:
    primeiro = endereco[0]
    ip = f'{endereco[0]}.{endereco[1]}.{endereco[2]}.{endereco[3]}'

    if primeiro >= 1 and primeiro <= 126:

        if primeiro == 10:
            print(f'{ip}: classe A, privado')
        else:
            print(f'{ip}: classe A, público')

    elif primeiro == 127:

        print(f'{ip}: loopback')

    elif primeiro >= 128 and primeiro <= 191:

        if primeiro == 172 and endereco[1] >= 16 and endereco[1] <= 31:
            print(f'{ip}: classe B, privado')
        else:
            print(f'{ip}: classe B, público')

    elif primeiro >= 192 and primeiro <= 223:

        if primeiro == 192 and endereco[1] == 168:
            print(f'{ip}: classe C, privado')
        else:
            print(f'{ip}: classe C, público')

    elif primeiro >= 224 and primeiro <= 239:

        print(f'{ip}: classe D (multicast)')

    else:

        print(f'{ip}: classe E (experimental)')