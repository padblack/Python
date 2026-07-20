#Lista de compras com possibilidade de inserir,apagar, listar
import os


lista = []

while True:
    opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("i")
        produto = input("O que deseja inserir? ")
        lista.append(produto)

    elif opcao == "a":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("a")
        apagar = input("Qual indice deseja apagar? ")
        
        try:
            indice = int(apagar)
            del lista[indice]
        except ValueError:
            print("Digite um numero inteiro")
        except IndexError:
            print("Esse valor não tem esse produto")

    elif opcao == "l":
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, valor in enumerate(lista):
            print(i, valor)
        