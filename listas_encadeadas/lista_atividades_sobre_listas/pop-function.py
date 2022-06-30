from listas_encadeadas.lista_encadeada import LinkedList

list = LinkedList()

list.preencherAleatoriamente(6)

print(list)

value = list.pop()

print(list)

list.popValue(list[2])

print(list)
