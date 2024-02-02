class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if len(self.saques) < 3:
            if valor <= 500:
                if self.saldo >= valor:
                    self.saques.append(valor)
                    self.saldo -= valor
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('O valor do saque não pode ser superior a R$ 500.00.')
        else:
            print('Limite diário de saques atingido.')

    def extrato(self):
        if self.depositos or self.saques:
            print('Extrato:')
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')
        else:
            print('Não foram realizadas movimentações.')


# Testando o sistema
if __name__ == "__main__":
    banco = Banco()

    banco.depositar(1000)
    banco.depositar(500.50)
    banco.sacar(200)
    banco.sacar(700)
    banco.sacar(400)
    banco.sacar(300)
    banco.extrato()
