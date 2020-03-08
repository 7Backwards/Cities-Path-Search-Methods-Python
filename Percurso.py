from Pessoa import Pessoa


class Percurso(Pessoa):

    pessoa = Pessoa

    def __init__(self, pessoa):
        """Construtor de percurso"""
        self.pessoa = pessoa

