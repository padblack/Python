nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))
espaco = False
quantidade = 0
if nome and idade:
    print(f"Seu nome é {nome}")
    nome_invertido = nome[::-1]
    print(f"Seu nome invertido é {nome_invertido}")
    if " " in nome:
        espaco = True
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")
    if espaco == True:
        quantidade = len(nome) - 1
    else:
        quantidade = len(nome)
    print(f"Seu nome tem {quantidade} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou algum campo vazio")
    