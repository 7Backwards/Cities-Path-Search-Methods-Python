from Pessoa import Pessoa


class Percurso(Pessoa):

    pessoa = Pessoa

    def __init__(self, pessoa):

        self.pessoa = pessoa

