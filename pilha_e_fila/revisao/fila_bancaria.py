class Fila():
    def __init__(self):
        self.dados = []

    def addValue(self, value):
        self.dados.append(value)

    def removeValue(self):
        if self.getSize() == 0:
            return -1
        else:
            return self.dados.pop(0)

    def getSize(self):
        return len(self.dados)

filaDeBanco = Fila()

controle = -1
while controle != 0:
    controle = int(input("1 para adicionar um cliente a fila;\n2 para realizar o atendimento do último cliente;\n0 para sair;\n"))

    if controle == 1:
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        numeroDeConta = input("Digite o numero de conta do cliente: ")

        dados = (nome, cpf, numeroDeConta)

        filaDeBanco.addValue(dados)
    if controle == 2:
        cliente = filaDeBanco.removeValue()

        if cliente == -1:
            print("\nLista vazia, adicione clientes!\n2")
        else:
            print("Cliente", cliente[0], "de cpf", cliente[1], "e conta", cliente[2], "foi atendido!\n")
