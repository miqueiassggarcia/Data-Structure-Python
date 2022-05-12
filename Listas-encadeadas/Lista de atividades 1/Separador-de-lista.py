from random import randint


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

    def __str__(self):
        return "[No " + str(self.data) + "] -> " + str(self.next)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.__size = 0

    def append(self, value):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next

            aux.next = Node(value)
        else:
            self.head = Node(value)

        self.__size += 1

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.head)

    def __getitem__(self, index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError("Posição não existe.")

            return aux.data
        else:
            raise IndexError("Lista vazia.")

    def __setitem__(self, index, value):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError("Posição não existe.")

            aux.data = value
        else:
            raise IndexError("Lista vazia.")

    def separateList(self, list):
        aux = list.head
        size = list.__size
        print(size//2)
        for i in range(size//2):
            aux = aux.next

        aux2 = aux.next
        aux.next = None

        return [list, aux2]


list = LinkedList()

for i in range(5):
    list.append(randint(0, 100))

print("Tamanho: " + str(len(list)))

print("Lista encadeada(" + str(list) + ")")

lists = list.separateList(list)

print("Nova lista encadeada(" + str(lists[0]) + ")")
print("Nova lista encadeada(" + str(lists[1]) + ")")
