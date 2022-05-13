from random import randint


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

    def __str__(self):
        return "[No " + str(self.data) + "] -> " + str(self.next)


class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__size = 0

    def setSize(self, value):
        self.__size = value

    def getHead(self):
        return self.__head

    def getSize(self):
        return self.__size

    def append(self, value):
        if self.__head:
            aux = self.__head
            while aux.next:
                aux = aux.next

            aux.next = Node(value)
        else:
            self.__head = Node(value)

        self.__size += 1

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__head)

    def __getitem__(self, index):
        if self.__head:
            aux = self.__head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError("Posição não existe.")

            return aux.data
        else:
            raise IndexError("Lista vazia.")

    def __setitem__(self, index, value):
        if self.__head:
            aux = self.__head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError("Posição não existe.")

            aux.data = value
        else:
            raise IndexError("Lista vazia.")

    def preencherAleatoriamente(self, quantidade):
        for i in range(quantidade):
            self.append(randint(0, 100))