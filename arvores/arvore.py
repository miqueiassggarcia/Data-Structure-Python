class BSTNode:
    def __init__(self, value=None):
        self.data = value
        self.left = self.right = None

    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def print_pre(self):
        if self.data:
            print(self.data, end=' ')
            if self.left:
                self.left.print_central()
            if self.right:
                self.right.print_central()

    def print_central(self):
        if self.data:
            if self.left:
                self.left.print_central()
            print(self.data, end=' ')
            if self.right:
                self.right.print_central()

    def print_pos(self):
        if self.data:
            if self.left:
                self.left.print_central()
            if self.right:
                self.right.print_central()
            print(self.data, end=' ')

    def total_nodes(self):
        if not self.data:
            return 0
        else:
            # if self.left:
            #    left = self.left.total_nodes()
            # else:
            #    left = 0
            # if self.right:
            #    right = self.right.total_nodes()
            # else:
            #    right = 0
            # return left + right + 1

            return (self.left.total_nodes() if self.left else 0) + (self.right.total_nodes() if self.right else 0) + 1

    def altura(self):
        if not self.data:
            return -1
        else:
            esquerda = self.left.altura() if self.left else -1
            direita = self.right.altura() if self.right else -1
            return esquerda + 1 if esquerda > direita else direita + 1

    def imprimir_graus(self):
        if self.data:
            # if self.right and self.left:
            #    print(self.data, "grau 2")
            # elif self.right or self.left:
            #    print(self.data, "grau 1")
            # else:
            #    print(self.data, "grau 0")
            print(self.data,
                  "grau 2" if self.right and self.left else "grau 1" if self.left or self.right else "grau 0"
                  )
            if self.left:
                self.left.imprimir_graus()
            if self.right:
                self.right.imprimir_graus()

    def imprimir_folhas(self):
        if self.data:
            if self.left:
               left = self.left.imprimir_folhas()
            else:
                left = 0
            if self.right:
               right = self.right.imprimir_folhas()
            else:
                right = 0
            if left + right == 0:
                folhas = 1
            else:
                folhas = 0
            return folhas + left + right


tree = BSTNode()

values = [20, 33, 9, 18, 41, 26, 3, 12, 29, 10, 44, 45, 42]

for value in values:
    tree.insert(value)

print("\nPre-ordem: ", end="")
tree.print_pre()
print("\nOrdem central: ", end="")
tree.print_central()
print("\nPos-ordem: ", end="")
tree.print_pos()

print('\nTotal de nós:', tree.total_nodes())
print('Altura:', tree.altura())

print("\nGraus dos nós")
tree.imprimir_graus()

print("\nQuantidade de folhas", tree.imprimir_folhas())
