from datetime import datetime
from random import randint
import pytz


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos: 
        nome (str): Nome do cliente
        cpf (str): CPF do cliente
        agencia: Agência responsável pela conta do cliente
        num_conta : Número da conta do cliente
        saldo: Saldo da conta do cliente
        limite: Limite de cheque especial do cliente
        transacoes: Histórico de transações do cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de {:,.2f}'.format(self._limite_conta()))
    
    def consultar_historico_transacoes(self):
        print('Histórico de transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


#Programa
conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44', 1234, 34062)

cartao_Gabriel = CartaoCredito('Gabriel', conta_Gabriel)
print(cartao_Gabriel.conta_corrente._num_conta)

print(cartao_Gabriel.numero)
print(cartao_Gabriel.cod_seguranca) 
print(cartao_Gabriel.validade)
