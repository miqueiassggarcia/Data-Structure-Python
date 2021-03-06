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

    def append(self, value):
        if self.__head:
            aux = self.__head
            while aux.next:
                aux = aux.next

            aux.next = Node(value)
        else:
            self.__head = Node(value)

        self.__size += 1

    def getItemByValueWithPrev(self, value):
        anterior = self.__head
        elemento = self.__head.next

        while elemento and elemento.data != value:
            anterior = elemento
            elemento = elemento.next
        if elemento:
            return [anterior, elemento]
        else:
            return -1

    def getItemByIndexWithPrev(self, index):
        if index < self.getSize():
            anterior = self.__head
            elemento = self.__head.next

            for i in range(1, self.__size):
                if i == index:
                    return [anterior, elemento]
                elif elemento:
                    anterior = elemento
                    elemento = elemento.next
            return -1
        else:
            raise IndexError("Posição não existe")

    def popValue(self, *value):
        if self.__head:
            if len(value) == 0:
                self.removeLastItem()

            elif self.__head.data == value[0]:
                self.removeFirstItem()

            else:
                values = self.getItemByValueWithPrev(value[0])
                if values != -1:
                    values[0].next = values[1].next
                    values[1].next = None
                    del values[1]
                    self.__size -= 1
        else:
            raise IndexError("Lista vazia!")

    def pop(self, *index):
        if self.__head:
            if len(index) == 0:
                self.removeLastItem()

            elif 0 == index[0]:
                self.removeFirstItem()

            else:
                values = self.getItemByIndexWithPrev(index[0])
                values[0].next = values[1].next
                values[1].next = None
                del values[1]
        else:
            raise IndexError("Lista vazia!")

    def insert(self, value, index):
        if self.__head:
            if self.__head:
                newElement = Node(value)
                if 0 == index:
                    aux = self.__head

                    self.__head = newElement
                    newElement.next = aux
                elif 1 == index:
                    aux = self.__head.next

                    self.__head.next = newElement
                    newElement.next = aux
                else:
                    values = self.getItemByIndexWithPrev(index)

                    values[0].next = newElement
                    newElement.next = values[1]
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
                self.setSize(self.getSize() - 1)
            else:
                del self.__head
                self.__head = None
                self.setSize(self.getSize() - 1)
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
                self.setSize(self.getSize() - 1)
            else:
                del self.__head
                self.__head = None
                self.setSize(self.getSize() - 1)
        else:
            raise IndexError("Lista vazia!")

    def print_partial(self, inicio, fim):
        if inicio > -1 and fim < self.getSize():
            string = "["
            for i in range(inicio, fim):
                if i == fim - 1:
                    string += str(self[i])
                else:
                    string += str(self[i]) + ", "

            string += "]"
            print(string)

    def printEvenNumbers(self):
        if self.__head:
            aux = self.__head
            while aux:
                if aux.data % 2 == 0:
                    print(aux.data, end=" ")
                aux = aux.next
        else:
            raise IndexError("Lista vazia!")

    def extend(self, list2):
        aux = self.__head
        while aux.next:
            aux = aux.next

        aux.next = list2
        self.setSize(self.__size + list2.__size)
        del list2

    def preencherAleatoriamente(self, quantidade):
        for i in range(quantidade):
            self.append(randint(0, 100))

    def preencherEmOrdem(self, quantidade):
        self.preencherAleatoriamente(quantidade)
        self.quick_sort(0, quantidade - 1)

    def quick_sort(self, start, end):
        if start >= end:
            return

        p = self.partition(start, end)
        self.quick_sort(start, p - 1)
        self.quick_sort(p + 1, end)

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

    def removeRepeatedValues(self):
        if self.__head:
            aux = self.__head
            value = aux.data
            while aux.next:
                aux = aux.next
                if aux.data == value:
                    self.popValue(value)
                else:
                    value = aux.data
