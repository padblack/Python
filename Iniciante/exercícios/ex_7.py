#Jogo estilo termo
import os

Palavra_secreta = "perfume"
letras_acertadas = ""
Contagem = 0
while True:
    letra = input()

    tamanho_letra = len(letra)
    if tamanho_letra > 1:
        print("Digite apenas uma letra")
        continue

    Contagem += 1
    
    if letra in Palavra_secreta:
        letras_acertadas += letra
    
    palavra = ""

    for letra_secreta in Palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra += letra_secreta
        else:
            palavra += "*"

    print(palavra)
    print(Contagem)

    if palavra == Palavra_secreta:
        break

print(f"Você ganhou depois de {Contagem} tentativas!!")


