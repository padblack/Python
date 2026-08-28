import ex_3_contas

class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, nome: str):
            self._nome = nome

        @property
        def idade(self):
            return self._idade
        
        @idade.setter
        def nome(self, idade: int):
            self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self, nome:str, idade:int):
        super().__init__(nome,idade)
        self.conta : ex_3_contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Paulo', 22)
    c1.conta = ex_3_contas.Conta_Corrente(111,10,100,50)
    print(c1.conta)
    print(c1)
    