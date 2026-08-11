#Dados do Exercicio 1
#Mandar os dados para um arquivo .json
import json
CAMINHO_ARQUIVO = "ex_1.json"

class Pessoa:
    def __init__(self,nome,idade,cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

p1 = Pessoa("Paulo", 20, "Preto")
p2 = Pessoa("João", 35, "Branco")
p3 = Pessoa("Jorge", 27, "Amarelo")
lista = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(lista, arquivo, ensure_ascii= False, indent=2)