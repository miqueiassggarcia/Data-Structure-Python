from listas_encadeadas.lista_encadeada import LinkedList

def quicksort(list):
    return list

def unirListasEncadeadas(list1, list2):
    aux1 = list1.getHead()
    aux2 = list2.getHead()

    newList = LinkedList()
    if list2.getSize() < list1.getSize():
        size = list1.getSize()
    else:
        size = list2.getSize()

    for i in range(size):
        if aux1:
            newList.append(aux1[i])
        if aux2:
            newList.append(aux2[i])

    newList = quicksort(newList)

list1 = LinkedList
list2 = LinkedList

list1.preencherEmOrdem(20)
list2.preencherEmOrdem(20)

print("Lista 1", list1)
print("Lista 2", list2)

unirListasEncadeadas(list1, list2)
