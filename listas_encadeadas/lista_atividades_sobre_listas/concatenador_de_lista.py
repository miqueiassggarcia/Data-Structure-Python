from random import randint
from listas_encadeadas.lista_encadeada import LinkedList


def linkingList(list1, list2):
    aux = list1.getHead()
    while (aux.next):
        aux = aux.next

    aux.next = list2
    list1.setSize(list1.getSize() + list2.getSize())
    del list2

list1 = LinkedList()
list2 = LinkedList()

for i in range(4):
    list1.append(randint(0, 100))
    list2.append(randint(0, 100))

print("Tamanho: " + str(len(list1)))
print("Lista encadeada 1(" + str(list1) + ")\n")
print("Tamanho: " + str(len(list2)))
print("Lista encadeada 2(" + str(list2) + ")\n")

linkingList(list1, list2)

print("Novo tamanho: " + str(len(list1)))
print(print("Lista unidas(" + str(list1) + ")\n"))
