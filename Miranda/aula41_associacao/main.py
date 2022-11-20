from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Diogo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
