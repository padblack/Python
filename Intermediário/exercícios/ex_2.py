#Duplicar,Triplicar e Quadriplicar um número usando Closure

def multiplicador(multiplicador):
    def multiplicado(numero):
        return numero * multiplicador
    return multiplicado

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

numero = int(input())
print(f"O dobro de {numero} é {duplicar(numero)}")
print(f"O triplo de {numero} é {triplicar(numero)}")
print(f"O quadruplo de {numero} é {quadriplicar(numero)}")
