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
            return (self.left.total_nodes() if self.left else 0) + (self.right.total_nodes() if self.right else 0) + 1

    def altura(self):
        if not self.data:
            return -1
        else:
            esq = self.left.altura() if self.left else -1
            dir = self.right.altura() if self.right else -1
            return esq + 1 if esq > dir else dir + 1


tree = BSTNode()

values = [20, 33, 9, 18, 41, 26, 3, 12, 29, 10, 44]

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
