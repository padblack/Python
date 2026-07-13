def teste(numero):
    if numero > 0:
        return "Numero positivo"
    else:
        return "Numero não positivo"
numero = int(input())
print(teste(numero))
#testando um número postivo e um número negativo

def teste_nome(nome):
    nome_inverso = nome[::-1]
    return nome_inverso
print(teste_nome("João"))
