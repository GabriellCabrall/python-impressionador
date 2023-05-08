from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de {:,.2f}'.format(self._limite_conta()))
    
    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))



conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44', 1234, 34062)
conta_Gabriel.consultar_saldo()

# Depositando dinheiro na conta
conta_Gabriel.depositar(10000)
conta_Gabriel.consultar_saldo()

print('Saldo final')
conta_Gabriel.consultar_saldo()

conta_Gabriel.consultar_limite_chequeespecial()

print('-' * 20)
conta_Gabriel.consultar_historico_transacoes()

print('-' * 20)
conta_Sandra = ContaCorrente('Sandra', '222.472.058.12', 55, 39202)

conta_Gabriel.transferir(1000, conta_Sandra)

conta_Gabriel.consultar_saldo()
conta_Sandra.consultar_saldo()

conta_Gabriel.consultar_historico_transacoes()
conta_Sandra.consultar_historico_transacoes()
