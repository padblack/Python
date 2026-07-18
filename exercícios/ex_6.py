#Transformar nome como *n*o*m*e
nome = input()
tamanho_nome = len(nome)
novo_nome = ""
contador = 0
while contador < tamanho_nome:
    novo_nome += "*"
    novo_nome += nome[contador]
    contador += 1
print(novo_nome)