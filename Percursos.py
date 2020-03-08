import Percurso


class Percursos:

    historicoPercursos = [Percurso]

    def limparHistorico(self):
        self.historicoPercursos.clear()

    def adicionarPercurso(self, percurso):
        self.historicoPercursos.append(percurso)
