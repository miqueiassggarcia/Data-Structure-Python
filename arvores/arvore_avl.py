class ArvoreAVL:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def getHeight(self):
        if not self:
            return 0

        return self.height

    def getBalance(self):
        if not self:
            return 0

        return self.left.getBalance() - self.right.getBalance()

    def print_central(self):
        if not self:
            return 0

        if self.left:
            self.left.print_central()
        print(self.value)
        if self.right:
            self.right.print_central()

    def left_rotate(self):
        aux_right = self.right
        aux = aux_right.left

        aux_right.left = self
        self.right = aux

        self.height = 1 + max(self.left.getHeight() if self.left else 0, self.right.getHeight() if self.right else 0)
        aux_right.height = 1 + max(aux_right.left.getHeight() if aux_right.left else 0, aux_right.right.getHeight() if aux_right.right else 0)

        return aux_right

    def right_rotate(self):
        aux_left = self.left
        aux = aux_left.right

        aux_left.right = self
        self.left = aux

        self.height = 1 + max(self.left.getHeight() if self.left else 0, self.right.getHeight() if self.right else 0)
        aux_left.height = 1 + max(aux_left.left.getHeight() if aux_left.left else 0, aux_left.right.getHeight() if aux_left.right else 0)

    def insert(self, value):
        if not self.value:
            self.value = value
        elif value < self.value:
            if self.left:
                self.left.insert(value)
        else:
            if self.right:
                self.right.inser(value)

        self.height = 1 + max(self.left.getHeight() if self.left else 0, self.right.getHeight() if self.right else 0)

        balance = self.getBalance()

        if balance > 1 and value < self.left.value:
            return self.right_rotate()

        if balance < -1 and value > self.right.value:
            return self.left_rotate()

        if balance > 1 and value > self.left.value:
            if self.left:
                self.left = self.left.left_rotate()
            return self.right_rotate()

        if balance < -1 and value < self.right.value:
            if self.right:
                self.right = self.right.right_rotate()
            return self.left_rotate()

        return self
