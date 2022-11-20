class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Diogo', '99888-1234')
conta = Conta(c1.get_nome(), 12345, 0)

conta.deposita(100)
conta.saque(20)
conta.extrato()
