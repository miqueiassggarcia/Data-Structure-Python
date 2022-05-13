from random import randint


class Node:
    def __init__(self, value, previous) -> None:
        self.data = value
        self.next = None
        self.previous = previous


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.__size = 0

    def append(self, value):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next

            aux.next = Node(value, aux)
        else:
            self.head = Node(value, None)

        self.__size += 1

    def __len__(self):
        return self.__size

    def print_inverse(self):
        output = '['
        aux = self.head
        while aux.next:
            aux = aux.next
        while aux:
            if aux.previous:
                output += str(aux.data) + ", "
            else:
                output += str(aux.data)
            aux = aux.previous
        output += "]"
        return output

    def __str__(self):
        output = '['
        aux = self.head
        while aux:
            if aux.next:
                output += str(aux.data) + ", "
            else:
                output += str(aux.data)
            aux = aux.next
        output += "]"
        return output

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
