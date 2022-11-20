from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = datetime.today().year

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já esta falando.')
            return
        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode falar enquanto come.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


    @classmethod
    def por_ano_nascimento(cls,nome, ano_naascimento):
        idade = cls.ano_atual = ano_naascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand
