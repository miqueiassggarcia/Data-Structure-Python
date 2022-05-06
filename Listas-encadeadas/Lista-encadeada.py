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
        self.size = 0

    def append(self, value):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next

            aux.next = Node(value)
        else:
            self.head = Node(value)

        self.size += 1

    def __str__(self):
        return str(self.head)


list = LinkedList()

for i in range(20):
    list.append(randint(0, 100))

print("Tamanho: " + str(list.size))
print("Lista encadeada(" + str(list) + ")")