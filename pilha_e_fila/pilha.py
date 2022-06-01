class Pilha():
    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)

    def pop(self):
        return self.__data.pop()

    def isEmpty(self):
        return len(self.__data) == 0

def validarExpressao(expressao):
    pilhaParenteses = Pilha()
    pilhaColchetes = Pilha()
    pilhaChaves = Pilha()

    for i in expressao:
        if i == "(":
            pilhaParenteses.push(i)
        if i == "[":
            pilhaColchetes.push(i)
        if i == "{":
            pilhaChaves.push(i)
        if i == ")":
            if pilhaParenteses.isEmpty():
                return False
            pilhaParenteses.pop()
        if i == "]":
            if pilhaColchetes.isEmpty():
                return False
            pilhaColchetes.pop()
        if i == "}":
            if pilhaChaves.isEmpty():
                return False
            pilhaChaves.pop()


    return pilhaParenteses.isEmpty() and pilhaColchetes.isEmpty() and pilhaChaves.isEmpty()

string = "(({{[[]]}}))"
print(validarExpressao(string))
