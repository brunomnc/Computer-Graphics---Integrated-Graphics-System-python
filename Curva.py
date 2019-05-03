from Ponto import Ponto
from typing import List


class Curva:
    def __init__(self, _pontos: [Ponto], _nome: str = None):
        self.pontos = _pontos
        self.nome = _nome
        self.pontos_bezier = self.calcula_pontos_bezier()

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

    def calcula_pontos_bezier(self):
        lista_pontos = self.pontos

        pontos_convertidos = []

        t = 0
        i = 0
        while i < len(lista_pontos):
            while t < 1:
                _x = (pow(1 - t, 3) * lista_pontos[i + 0].x) + \
                     (3 * t * pow(1 - t, 2) * lista_pontos[i + 1].x) + \
                     (3 * pow(t, 2) * (1 - t) * lista_pontos[i + 2].x) + \
                     (pow(t, 3) * lista_pontos[i + 3].x)

                _y = (pow(1 - t, 3) * lista_pontos[i + 0].y) + \
                     (3 * t * pow(1 - t, 2) * lista_pontos[i + 1].y) + \
                     (3 * pow(t, 2) * (1 - t) * lista_pontos[i + 2].y) + \
                     (pow(t, 3) * lista_pontos[i + 3].y)

                p = Ponto(_x, _y)

                pontos_convertidos.append(p)

                t += 0.05
            i = i + 4

        return pontos_convertidos

