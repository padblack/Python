Tirar formato de lista no print = print(*lista)

Tirar o espaço entre = , sep="".

Juntar strings = "".join(lista).

eval = Tipo de print que possibilita escrever funções com imput(Ex.: print(5 + 2))

sorted = Pega uma lista e ordena, sem mexer na original

set = tira os numeros repetidos em uma lista

lambda = cria mini funções

sorted + lambda = Serve para ordenar dados(Ex.: matriz_tal = sorted(matriz_original, key = lambda x : x[variavel])

all = todas as condiçoes precisão ser aceitas para retornar um true(Ex.: all(i > 0 for i in lista))

any = 1 condição precisa ser aceita para retornar um true(Ex.: any(str(i) == str(i)[::-1] for i in lista))

not in = saber se tal valor/matriz não está dentro de uma matriz

List Comprehension = matriz_final = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if tal tal], faz um loop dentro de uma lista

lista com map = lista = list(map(int, input().split()))