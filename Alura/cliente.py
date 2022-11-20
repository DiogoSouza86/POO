class Cliente:
    def __init__(self, nome):
        self.__nome = nome


    #chama um atributo por um metodo mas sem usaar parentesis
    #usado como getter mas sem o "get_"
    @property
    def nome(self):
        print("Chamando property")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome")
        self.__nome =  nome



