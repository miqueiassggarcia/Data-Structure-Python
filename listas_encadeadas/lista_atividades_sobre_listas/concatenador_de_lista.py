from listas_encadeadas.lista_encadeada import LinkedList

list1 = LinkedList()
list2 = LinkedList()

list1.preencherAleatoriamente(2)
list2.preencherAleatoriamente(2)

print("Tamanho: " + str(len(list1)))
print("Lista encadeada 1(" + str(list1) + ")\n")
print("Tamanho: " + str(len(list2)))
print("Lista encadeada 2(" + str(list2) + ")\n")

list1.linkingLists(list2)

print("Novo tamanho: " + str(len(list1)))
print(print("Lista unidas(" + str(list1) + ")\n"))
