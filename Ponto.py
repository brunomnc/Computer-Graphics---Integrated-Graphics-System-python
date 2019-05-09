from numpy import array

class Ponto:
    def __init__(self, _x, _y, _nome=None, selected = False):
        self.x = _x
        self.y = _y
        self.nome = _nome
        self.m = self.to_matrix()
        self.selecionado = selected

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
        return 'Ponto'

    def get_centro_gravidade(self):
        return self.x, self.y

    def to_matrix(self):
        m = array([[self.x, 0],
                   [0, self.y]])

        return m

