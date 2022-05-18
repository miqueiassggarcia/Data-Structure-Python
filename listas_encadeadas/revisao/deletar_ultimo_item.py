from listas_encadeadas.lista_encadeada import LinkedList

list = LinkedList()

#list.removeLastItem()

list.append(10)

print(list)

list.removeLastItem()

print(list)

list.preencherAleatoriamente(5)

print("Lista inicial:", list)

list.removeLastItem()

print("Lista depois:", list)
