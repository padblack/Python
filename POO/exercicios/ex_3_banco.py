import ex_3_contas
import ex_3_pessoa

class Banco():
    def __init__(
            self,
            agencias: list[int] | None=None,
            clientes: list[ex_3_pessoa.Pessoa] | None=None,
            contas: list[ex_3_contas.Conta] | None=None
        ):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_conta(self,conta):
        if conta in self.contas:
            return True
        return False

    def _checa_agencia(self,conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checa_cliente(self,cliente):
        if cliente in self.clientes:
            return True
        return False
        
    def autenticar(self, cliente, conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)

    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
            return f'{class_name}{attrs}'
if __name__ == '__main__':
    c1 = ex_3_pessoa.Cliente('Paulo', 22)
    c1.conta = ex_3_contas.Conta_Corrente(111,10,100,50)
    banco = Banco()
    print(banco)
        