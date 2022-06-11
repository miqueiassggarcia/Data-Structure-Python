class Disciplinas:
    def __init__(self, nome):
        self.nome = nome
        self.next = None

class Alunos:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = None
        self.next = None

    def adicionarDisciplina(self, nome):
        if self.disciplinas:
            aux = self.disciplinas
            while aux.next:
                aux = aux.next
            aux.next = Disciplinas(nome)

        else:
            self.disciplinas = Disciplinas(nome)

class Universidades:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = None
        self.next = None

    def adicionarAlunos(self, nome):
        if self.alunos:
            aux = self.alunos
            while aux.next:
                aux = aux.next
            aux.next = Alunos(nome)
        else:
            self.alunos = Alunos(nome)

    def imprimirAlunos(self):
        aux = self.alunos
        while aux:
            print("\nAluno:", aux.nome)
            aux2 = aux.disciplinas
            print("Disciplinas:")
            while aux2:
                print(aux2.nome, ";", sep="")
                aux2 = aux2.next
            aux = aux.next



class Multilista:
    def __init__(self):
        self.head = None

    def buscarUniversidade(self, universidade):
        if self.head:
            aux = self.head
            while aux and aux.nome != universidade:
                aux = aux.next
            return aux
        return None

    def buscarAluno(self, universidade, aluno):
        if self.head:
            aux = self.buscarUniversidade(universidade)
            if aux:
                aux = aux.alunos
                if aux:
                    while aux and aux.nome != aluno:
                        aux = aux.next
                    return aux
        return None

    def cadastrarUniversidade(self, nome):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Universidades(nome)
        else:
            self.head = Universidades(nome)

    def cadastrarAluno(self, nome, universidade):
        if self.head:
            aux = self.buscarUniversidade(universidade)
            if aux:
                aux.adicionarAlunos(nome)

    def cadastrarDisciplina(self, nome, universidade, aluno):
        if self.head:
            aux = self.buscarAluno(universidade, aluno)
            if aux:
                aux.adicionarDisciplina(nome)

    def imprimirUniversidades(self):
        if self.head:
            aux = self.head
            while aux:
                print("\nUniversidade:", aux.nome)
                aux.imprimirAlunos()
                aux = aux.next

multilista = Multilista()

multilista.cadastrarUniversidade("UEPB")
multilista.cadastrarUniversidade("UFPB")
multilista.cadastrarAluno("MIQUEIAS", "UEPB")
multilista.cadastrarAluno("BRUNO", "UFPB")
multilista.cadastrarDisciplina("ESTRUTURA DE DADOS", "UEPB", "MIQUEIAS")
multilista.cadastrarDisciplina("ALGEBRA LINEAR", "UEPB", "MIQUEIAS")
multilista.cadastrarDisciplina("CALCULO 1", "UFPB", "BRUNO")
multilista.cadastrarDisciplina("METODOLOGIA CIENTIFICA", "UFPB", "BRUNO")
multilista.imprimirUniversidades()
