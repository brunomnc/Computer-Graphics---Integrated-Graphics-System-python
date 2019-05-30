from numpy import array
from Ponto import Ponto


class Reta:
    def __init__(self, _x1, _y1, _x2, _y2, _nome=None, selected = False):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2
        self.pontos = [Ponto(_x1, _y1), Ponto(_x2, _y2)]
        self.m = self.to_matrix()
        self.nome = _nome
        self.selecionado = selected

    def __str__(self):
        return 'Reta'

    def get_sttributes(self):
        return str(self), self.nome

    def get_centro_gravidade(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def __eq__(self, other):
        if self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2 and self.nome == other.nome:
            return True
        else:
            return False

    def to_matrix(self):
        m = array([[self.x1, self.x2, 0],
               [self.y1, self.y2, 0],
               [0,0,1]])
        return m


