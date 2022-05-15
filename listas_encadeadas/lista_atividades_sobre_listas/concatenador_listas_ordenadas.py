from listas_encadeadas.lista_encadeada import LinkedList

def unirListasEncadeadas(list1, list2):
    newList = LinkedList()

    for i in range(list1.getSize()):
        newList.append(list1[i])

    for i in range(list2.getSize()):
        newList.append(list2[i])

    newList.quick_sort(0, newList.getSize() - 1)

    value = None
    aux = newList.getHead()
    index = 0

    while aux:
        if value != newList[index]:
            value = newList[index]
            aux = aux.next
            index += 1
        else:
            newList.pop(value)
            aux = aux.next

    return newList


list1 = LinkedList()
list2 = LinkedList()

list1.preencherEmOrdem(150)
list2.preencherEmOrdem(100)

print("Tamanho:", list1.getSize())
print("Lista 1", list1)
print("Tamanho:", list2.getSize())
print("Lista 2", list2)

newList = unirListasEncadeadas(list1, list2)

print("\nTamanho:", newList.getSize())
print("Nova lista", newList)