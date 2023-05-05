class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar_dinheiro(self, valor):
        self.saldo -= valor


conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44')
conta_Gabriel.consultar_saldo()

# Depositando dinheiro na conta
conta_Gabriel.depositar(10000)
conta_Gabriel.consultar_saldo()

# Sacando dinheiro da conta
conta_Gabriel.sacar_dinheiro(2500)
conta_Gabriel.consultar_saldo()