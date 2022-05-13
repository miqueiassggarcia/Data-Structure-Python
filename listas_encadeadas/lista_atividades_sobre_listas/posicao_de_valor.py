from listas_encadeadas.lista_encadeada import LinkedList

def getPosition(list, value):
    for i in range(list.getSize()):
        if list[i] == value:
            return i

    return -1

list = LinkedList()

list.preencherAleatoriamente(100)

position = getPosition(list, 20)

if position != -1:
    print("O valor 20 foi encontrado na posição:", position)
else:
    print("O valor 20 não está contido na lista.")