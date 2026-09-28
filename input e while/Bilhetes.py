idade = input("Qual a sua Idade?: ")
idade = int(idade)

if idade < 3:
    print("Grátis")
elif 3 <= idade <= 12:
    print("10€")
else:
    print("15€")
