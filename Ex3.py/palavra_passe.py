utilizador = 'marta'
palavra_passe = 'MARTA'
comuns = ['123456', 'password', 'qwerty', 'admin123', 'abc123']

valida = True
comuns_min = []

if len(palavra_passe) < 8:
    print("ter pelo menos 8 caracteres")
    valida = False

if palavra_passe.lower() == palavra_passe:
    print("Nao tem letras maiusculas")
    valida = False

if palavra_passe.upper() == palavra_passe:
    print("Nao tem letras minusculas")
    valida = False

if utilizador.lower() == palavra_passe.lower():
    print("Palavra-passe nao pode ser igual ao nome de utilizador")
    valida = False

for palavra in comuns:
    comuns_min.append(palavra.lower())

if palavra_passe.lower() in comuns_min:
    print("Palavra-passe nao e forte")
    valida = False

if valida:
    print("Palavra-passe valida")
else:
    print("Palavra-passe rejeitada")