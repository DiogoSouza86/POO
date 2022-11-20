from classes import *

c1 = Cliente('Diogo', 35)
c1.insere_endereco('Salvador', 'BA')
c1.insere_endereco('Brasilia', 'DF')
print(c1.nome)
c1.lista_enderecos()
print()

c2 = Cliente('Luiz', 55)
c2.insere_endereco('Belo Horizonte', 'MG')
print(c2.nome)
c2.lista_enderecos()