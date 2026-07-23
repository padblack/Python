#Validar CPF
#Conta do primeiro digito:
cpf = "746.824.890-70"
numeros = []
numeros_multiplicados = []
soma_digito1 = 0
soma_digito2 = 0

for i in cpf:
    if i == "." or i == "-":
        continue
    else:
        numero = int(i)
        numeros.append(numero)



Contagem_1 = 10

for x in range(len(numeros)):
    multiplicacao = numeros[x] * Contagem_1
    Contagem_1 -= 1
    numeros_multiplicados.append(multiplicacao)

numeros_multiplicados_1 = numeros_multiplicados[:-2]

for b in numeros_multiplicados_1:
    soma_digito1 += b

resultado = (soma_digito1 * 10) % 11
digito_1 = 0 if resultado > 9 else resultado

print(f"O primeiro digito do seu CPF é {digito_1}")
        
# print(numeros)
# print(numeros_multiplicados_1)
# print(soma_digito1)
# print(resultado)
# print(digito_1)

#Conta do Segundo Digito:

numeros_multiplicados_2 = numeros[:-1]

Contagem_2 = 11

for j in range(len(numeros_multiplicados_2)):
    numeros_multiplicados_2[j] *= Contagem_2
    soma_digito2 += numeros_multiplicados_2[j]
    Contagem_2 -= 1

# print(soma_digito2)

resultado_2 = (soma_digito2 * 10) % 11
digito_2 = 0 if resultado_2 > 9 else resultado_2

print(resultado_2)
print(f"O segundo digito do seu CPF é {digito_2}")


