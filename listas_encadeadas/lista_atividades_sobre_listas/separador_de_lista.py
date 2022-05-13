from listas_encadeadas.lista_encadeada import LinkedList

def separateList(list):
    aux = list.getHead()
    size = list.getSize() - 1

    for i in range(size // 2):
        aux = aux.next

    aux2 = aux.next
    aux.next = None

    return [list, aux2]

list = LinkedList()

list.preencherAleatoriamente(5)

print("Tamanho: " + str(len(list)))

print("Lista encadeada(" + str(list) + ")")

lists = separateList(list)

print("\nNova lista encadeada(" + str(lists[0]) + ")")
print("Nova lista encadeada(" + str(lists[1]) + ")")
