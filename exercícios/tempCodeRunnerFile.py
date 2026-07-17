"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input()
# try:
#     numero_int = int(numero)
# except:
#     print("Numero não inteiro")

# if (numero_int % 2) == 0:
#     print("Numero par")
# else:
#     print("Numero impar")


horas = int(input())
if horas <= 11 and horas >= 0:
    print("Bom dia")
elif horas <= 17 and horas >= 12:
    print("Boa tarde")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""