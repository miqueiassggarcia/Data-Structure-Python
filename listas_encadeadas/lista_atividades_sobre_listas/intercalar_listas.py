from listas_encadeadas.lista_encadeada import LinkedList

def intercalarListas(list1, list2):
    if list1.getSize() == list2.getSize():
        list3 = LinkedList()
        for i in range(list1.getSize()):
            list3.append(list1[i])
            list3.append(list2[i])

        del list1
        del list2
        return list3
    else:
        print("\nListas contém tamanhos diferentes")
        return []


list1 = LinkedList()
list2 = LinkedList()

list1.preencherAleatoriamente(2)
list2.preencherAleatoriamente(2)

print("Lista 1", list1)
print("Lista 2", list2, "\n")

newList = intercalarListas(list1, list2)

print(newList)
