#Primeiro EX.:
numero = input()
try:
    numero_int = int(numero)
except:
    print("Numero não inteiro")

if (numero_int % 2) == 0:
    print("Numero par")
else:
    print("Numero impar")

#Segundo EX.:
horas = int(input())
if horas <= 11 and horas >= 0:
    print("Bom dia")
elif horas <= 17 and horas >= 12:
    print("Boa tarde")
else:
    print("Boa noite")

#Terceiro EX.:
nome = input()
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <=6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande ")