import abc

class Conta(abc.ABC):
    def __init__(self,agencia,conta,saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self,valor):...   

    def depositar(self,valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg = ''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

    

class Conta_Poupanca(Conta):
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print("Não foi possível sacar")
        self.detalhes(f'SAQUE NEGADO {valor}')


class Conta_Corrente(Conta):
    def __init__(self,agencia,conta,saldo=0,limite=0):
            super().__init__(agencia,conta,saldo)
            self.limite = - limite

    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= self.limite:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print("Não foi possível sacar")
        self.detalhes(f'(SAQUE NEGADO {valor})')

if __name__ == '__main__':
    # cp1 = Conta_Poupanca(111, 222, 0)
    # cp1.depositar(10)
    # cp1.sacar(5)
    # print('')

    cc1 = Conta_Corrente(100,300,0,100)
    cc1.depositar(0)
    cc1.sacar(101)

