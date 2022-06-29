class Venda:
    def __init__(self, nome, valor_total):
        self.nome = nome
        self.valor_total = valor_total
        self.next = None


class Supermercado:
    def __init__(self, nome):
        self.nome = nome
        self.total_vendas = 0
        self.vendas = None
        self.next = None

    def adicionarVenda(self, nome, valor_total):
        if self.vendas:
            aux = self.vendas
            while aux.next:
                aux = aux.next
            aux.next = Venda(nome, valor_total)
            self.total_vendas += valor_total
        else:
            self.vendas = Venda(nome, valor_total)
            self.total_vendas += valor_total

    def removerVenda(self, nome):
        if self.vendas:
            if self.vendas.nome == nome:
                if self.vendas.next:
                    aux = self.vendas
                    self.vendas = aux.next
                    aux.next = None
                    del aux
                else:
                    del self.vendas
                    self.vendas = None
            else:
                ant = None
                aux = self.vendas
                while aux and aux.nome != nome:
                    ant = aux
                    aux = aux.next
                if aux:
                    ant.next = aux.next
                    aux.next = None
                    del aux

    def imprimirVendas(self):
        if self.vendas:
            aux = self.vendas
            while aux:
                print(aux.nome, ": R$", aux.valor_total, sep="")
                aux = aux.next
        else:
            print("Não há vendas!")


class Multilista:
    def __init__(self):
        self.head = None

    def adicionarSupermercado(self, nome):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Supermercado(nome)
        else:
            self.head = Supermercado(nome)

    def removerSupermercado(self, nome):
        if self.head:
            if self.head.nome == nome:
                if self.head.next:
                    aux = self.head
                    self.head = aux.next
                    aux.next = None
                    del aux
                else:
                    del self.head
                    self.head = None
            else:
                ant = None
                aux = self.head
                while aux and aux.nome != nome:
                    ant = aux
                    aux = aux.next
                if aux:
                    ant.next = aux.next
                    aux.next = None
                    del aux

    def adicionarVenda(self, supermercado, nome, valor_total):
        if self.head:
            aux = self.head
            while aux and aux.nome != supermercado:
                aux = aux.next
            if aux:
                aux.adicionarVenda(nome, valor_total)

    def removerVenda(self, supermercado, nome):
        if self.head:
            aux = self.head
            while aux and aux.nome != supermercado:
                aux = aux.next
            if aux:
                aux.removerVenda(nome)

    def imprimirVendas(self, supermercado):
        if self.head:
            aux = self.head
            while aux and aux.nome != supermercado:
                aux = aux.next
            if aux:
                print("\n", aux.nome, sep="")
                aux.imprimirVendas()


lista = Multilista()

lista.adicionarSupermercado("atacadao")
lista.adicionarVenda("atacadao", "alcool", 15)
lista.adicionarVenda("atacadao", "xampu", 85)
lista.adicionarVenda("atacadao", "banana", 20)

lista.imprimirVendas("atacadao")

lista.adicionarSupermercado("mercadinho")
lista.adicionarVenda("mercadinho", "alcool", 15)
lista.adicionarVenda("mercadinho", "xampu", 85)
lista.adicionarVenda("mercadinho", "banana", 20)

lista.imprimirVendas("mercadinho")

lista.removerVenda("mercadinho", "alcool")
lista.removerVenda("mercadinho", "xampu")

lista.imprimirVendas("mercadinho")

lista.removerSupermercado("atacadao")
lista.removerVenda("atacadao", "xampu")

lista.imprimirVendas("mercadinho")
