class Pilha():
    def __init__(self):
        self.dados = []

    def getSize(self):
        return len(self.dados)

    def addValue(self, value):
        self.dados.append(value)

    def removeValue(self):
        if self.getSize() == 0:
            return -1
        else:
            return self.dados.pop(self.getSize() - 1)

pilhaPalavra = Pilha()

palavra = input("Digite uma palavra: ")

for i in palavra:
    pilhaPalavra.addValue(i)

palavraReversa = ""

for i in range(pilhaPalavra.getSize()):
    palavraReversa += pilhaPalavra.removeValue()

print("\nPalavra original:", palavra, "palavra inversa:", palavraReversa)
