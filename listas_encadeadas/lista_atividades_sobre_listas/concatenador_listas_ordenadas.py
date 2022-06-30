from listas_encadeadas.lista_encadeada import LinkedList


def unirListasEncadeadas(list1, list2):
    newList = LinkedList()

    for i in range(list1.getSize()):
        newList.append(list1[i])

    for i in range(list2.getSize()):
        newList.append(list2[i])

    newList.quick_sort(0, newList.getSize() - 1)

    print("Tamanho original:", newList.getSize())
    print("Nova lista original", newList)

    newList.removeRepeatedValues()

    return newList


lista1 = LinkedList()
lista2 = LinkedList()

lista1.preencherEmOrdem(150)
lista2.preencherEmOrdem(150)

print("Tamanho:", lista1.getSize())
print("Lista 1", lista1)
print("Tamanho:", lista2.getSize())
print("Lista 2", lista2)

newList = unirListasEncadeadas(lista1, lista2)

print("\nTamanho:", newList.getSize())
print("Nova lista", newList)
