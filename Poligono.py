from Ponto import Ponto
from typing import List


class Poligono:
    def __init__(self, _pontos: [Ponto], _nome: str = None):
        self.pontos = _pontos
        self.nome = _nome

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
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

