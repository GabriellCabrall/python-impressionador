from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R${:,.2f}'.format(self.caixa))
        else:
            print('O valor do caixa está ok. Caixa atual: R${:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Sem dinheiro pra emprestar')
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
# ===================================================================================================

class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        if self.caixa > valor:
            self.caixa -= valor
            self.caixa_paypal += valor
            print('Transferência concluída\nValor do caixa: R${:,.2f}\nValor paypal:R${:,.2f}'.format(self.caixa, self.caixa_paypal))
        else:
            print('Valor de caixa insuficiente para a transferência!')

    def sacar_paypal(self, valor):
        if self.caixa_paypal > valor:
            self.caixa_paypal -= valor
            self.caixa += valor
            print('Transferência concluída\nValor do caixa: R${:,.2f}\nValor paypal:R${:,.2f}'.format(self.caixa, self.caixa_paypal))
        else:
            print('Valor de caixa do paypal insuficiente para a transferência!')
# ===================================================================================================

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000
# ===================================================================================================

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000



#Código

agencia1 = Agencia(20203891, 2040281039, 3748)

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com', 22224444, 1921000000)
agencia_virtual.verificar_caixa()

agencia_comum = AgenciaComum(33332222, 323422222)
agencia_premium = AgenciaPremium(22918493, 3920000010)

agencia_virtual.sacar_paypal(20000)

