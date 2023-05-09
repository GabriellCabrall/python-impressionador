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


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000


class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass



agencia1 = Agencia(20203891, 2040281039, 3748)

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com', 22224444, 1921000000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.clientes)
