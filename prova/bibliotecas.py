class Livros:
    def __init__(self, nome):
        self.nome = nome
        self.next = None


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.livros = None
        self.next = None

    def adicionarLivro(self, livro):
        if self.livros:
            aux = self.livros
            while aux.next:
                aux = aux.next
            aux.next = Livros(livro)
        else:
            self.livros = Livros(livro)


class Biblioteca:
    def __init__(self):
        self.alunos = None

    def adicionarAluno(self, aluno):
        if self.alunos:
            aux = self.alunos
            while aux.next:
                aux = aux.next
            aux.next = Aluno(aluno)
        else:
            self.alunos = Aluno(aluno)

    def adicionarLivro(self, aluno, livro):
        if self.alunos:
            aux = self.alunos
            while aux and aux.nome != aluno:
                aux = aux.next
            if aux:
                aux.adicionarLivro(livro)


biblioteca = Biblioteca()
biblioteca.adicionarAluno("miqueias")
biblioteca.adicionarAluno("miqueias")
biblioteca.adicionarLivro("miqueias", "test")
biblioteca.adicionarLivro("miqueias", "test")
