class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * ( percentual/100 ))

    #GETTER - RECEBE UM VALOR
    @property
    def preço(self):
        return self._preço

    @property
    def nome(self):
        return self._nome

    #SETTER - CONFIGURA O GETTER. "valor" serve para atribuir o que sera modificado pela setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ''))
        self._preço = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title().strip()


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preço)

p2 = Produto('    caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preço)

p3 = Produto('FOGÃO', 500)
p3.desconto(10)
print(p3.nome, p3.preço)