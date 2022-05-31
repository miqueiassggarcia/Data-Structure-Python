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

    def pop(self, index):
        if self.__head:
            if not index:
                self.removeLastItem()

            elif self.__head:
                if self.__head.data == index:
                    aux = self.__head
                    self.__head = self.__head.next

                    aux.next = None
                    del aux
                    self.__size -= 1

                elif self.__head.next.data == index:
                    aux = self.__head.next
                    self.__head.next = self.__head.next.next

                    aux.next = None
                    del aux
                    self.__size -= 1

                else:
                    antepenultimo = self.__head
                    penultimo = self.__head.next
                    ultimo = self.__head.next.next

                    value_find = True
                    while ultimo and value_find:
                        aux = penultimo
                        penultimo = ultimo
                        antepenultimo = aux
                        ultimo = ultimo.next
                        if penultimo.data == index:
                            value_find = False

                    penultimo.next = None
                    del penultimo
                    antepenultimo.next = ultimo
                    self.__size -= 1

        else:
            raise IndexError("Lista vazia!")

    def seachItem(self, value):
        aux = self.__head

        exists = False

        while aux and not exists:
            if aux.data == value:
                exists = True
            aux = aux.next

        return exists

    def buscaBinaria(self, ini, fim, value):
        if ini <= fim:
            meio = (ini + fim) // 2

            if self[meio] == value:
                return meio
            elif ini == fim:
                return -1
            elif value > self[meio]:
                return self.buscaBinaria(meio + 1, fim, value)
            else:
                return self.buscaBinaria(ini, meio - 1, value)

        return -1

    def removeFirstItem(self):
        if self.__head:
            if self.__head.next:
                aux = self.__head
                self.__head = aux.next
                aux.next = None
                del aux
            else:
                del self.__head
                self.__head = None
        else:
            raise IndexError("Lista vazia!")

    def removeLastItem(self):
        if self.__head:
            if self.__head.next:
                aux = self.__head
                prev = None

                while aux.next:
                    prev = aux
                    aux = aux.next

                prev.next = None
                del aux
            else:
                del self.__head
                self.__head = None
        else:
            raise IndexError("Lista vazia!")

    def printOddNumbers(self):
        if self.__head:
            aux = self.__head
            while aux:
                if aux.data % 2 == 0:
                    print(aux.data, end=" ")
                aux = aux.next
        else:
            raise IndexError("Lista vazia!")

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__head)

    def __getitem__(self, index):
        if self.getHead():
            aux = self.getHead()
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError("Posição não existe.")

            return aux.data
        else:
            raise IndexError("Lista vazia.")

    def __setitem__(self, index, value):
        if self.getHead():
            aux = self.getHead()
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

    def preencherEmOrdem(self, quantidade):
        self.preencherAleatoriamente(quantidade)
        self.quick_sort(0, quantidade - 1)

    def partition(self, start, end):
        pivot = self[start]
        low = start + 1
        high = end

        while True:
            while low <= high and self[high] >= pivot:
                high = high - 1

            while low <= high and self[low] <= pivot:
                low = low + 1

            if low <= high:
                self[low], self[high] = self[high], self[low]
            else:
                break

        self[start], self[high] = self[high], self[start]

        return high

    def quick_sort(self, start, end):
        if start >= end:
            return

        p = self.partition(start, end)
        self.quick_sort(start, p - 1)
        self.quick_sort(p + 1, end)

    def linkingLists(self, list2):
        aux = self.getHead()
        while (aux.next):
            aux = aux.next

        aux.next = list2
        self.setSize(self.getSize() + list2.getSize())
        del list2
