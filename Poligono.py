from Ponto import Ponto
from numpy import array, append


class Poligono:
    def __init__(self, _pontos: [Ponto], _nome: str = None, selected=False):
        self.pontos = _pontos
        self.nome = _nome
        self.selecionado = selected
        self.m = self.to_matrix()

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
        if len(self.pontos) == 1:
            return 'Ponto'
        if len(self.pontos) == 2:
            return 'Reta'
        return 'Poligono'

    def at(self, index: int):
        return self.pontos[index]

    def get_centro_gravidade(self):
        x = 0
        y = 0
        for ponto in self.pontos:
            x += ponto.x
            y += ponto.y

        return x / len(self.pontos), y / len(self.pontos)

    def __eq__(self, other):
        if self.nome == other.nome:
            return True
        else:
            return False

    def to_matrix(self):
        m = array([])
        sz = len(self.pontos)
        if sz == 0:
            return

        for p in range(sz - 1):
            m = append(m, [[self.pontos[p].x, self.pontos[p].y, 0]])

        m = append(m, [[self.pontos[sz - 1].x, self.pontos[sz - 1].y, 1]])

        return m
