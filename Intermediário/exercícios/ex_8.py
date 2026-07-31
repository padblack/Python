#some valores de 2 listas
lista_1 = [1,2,3,4,5]
lista_2 = [3,4,5,6]

def somar_listas(l1,l2):
    menor = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(menor)
    ]

print(somar_listas(lista_1,lista_2))