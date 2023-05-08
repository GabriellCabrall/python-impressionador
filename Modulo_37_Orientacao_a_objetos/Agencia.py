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


agencia1 = Agencia(20203891, 2040281039, 3748)

agencia1.caixa = 1000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 4340804444, 10)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Gabriel', 20837452157, 10000)
print(agencia1.clientes)
