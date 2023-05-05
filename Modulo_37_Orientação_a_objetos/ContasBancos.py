class ContaCorrente:

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de {:,.2f}'.format(self._limite_conta()))


conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44', 1234, 34062)
conta_Gabriel.consultar_saldo()

# Depositando dinheiro na conta
conta_Gabriel.depositar(10000)
conta_Gabriel.consultar_saldo()

# Sacando dinheiro da conta
conta_Gabriel.sacar_dinheiro(1100)

print('Saldo final')
conta_Gabriel.consultar_saldo()

conta_Gabriel.consultar_limite_chequeespecial()
