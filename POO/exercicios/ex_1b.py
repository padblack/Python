import json
from ex_1a import CAMINHO_ARQUIVO, Pessoa, fazer_dump



with open (CAMINHO_ARQUIVO, "r") as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

    print(p1.nome)
    print(p2.nome)