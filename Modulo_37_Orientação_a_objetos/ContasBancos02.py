from datetime import datetime
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
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self._cartoes = []

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


class CartaoCredito:
    
    def __init__(self, titular, conta_corrente):
        self.numero = None
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente


#Programa
conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44', 1234, 34062)
conta_Gabriel.consultar_saldo()

cartao_Gabriel = CartaoCredito('Gabriel', conta_Gabriel)
print(cartao_Gabriel.conta_corrente.num_conta)
