from ContasBancos02 import ContaCorrente, CartaoCredito

#Programa
conta_Gabriel = ContaCorrente('Gabriel', '111.222.333-44', 1234, 34062)

cartao_Gabriel = CartaoCredito('Gabriel', conta_Gabriel)

conta_Gabriel._nome = 'Gabriel Cabral'
print(conta_Gabriel._nome)

cartao_Gabriel.senha = '1245'
print(cartao_Gabriel.senha)

print(conta_Gabriel.__dict__)
print(cartao_Gabriel.__dict__)
