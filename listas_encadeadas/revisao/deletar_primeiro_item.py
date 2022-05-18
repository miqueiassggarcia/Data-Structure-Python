from listas_encadeadas.lista_encadeada import LinkedList

list = LinkedList()

#list.removeFirstItem()

list.append(10)

print(list)

list.removeFirstItem()

print(list)

list.preencherAleatoriamente(10)

print("Lista inicial:", list)

list.removeFirstItem()

print("Lista depois:", list)
