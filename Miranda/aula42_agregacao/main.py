from classes import *

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa', 50)
p2 = Produto('Iphone', 1000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.listar_produtos()
print(carrinho.soma_total())
