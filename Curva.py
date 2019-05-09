from Ponto import Ponto
from math import fabs, pow


class Curva:
    def __init__(self, _pontos: [Ponto], _nome: str = None, bezier = False, selected = False):
        self.pontos = _pontos
        self.nome = _nome
        self.selecionado = selected
        if bezier == True:
            self.pontos_curva = self.calcula_pontos_bezier()
        if bezier == False:
            self.pontos_curva = self.calcula_pontos()

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
        return 'Curva'

    def at(self, index: int):
        return self.pontos[index]

    def get_centro_gravidade(self):
        x = 0
        y = 0
        for ponto in self.pontos_curva:
            x += ponto.x
            y += ponto.y

        return x / len(self.pontos_curva), y / len(self.pontos_curva)

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

    def calcula_pontos(self):
        i = 0
        pontos_convertidos = []

        while i + 3 < len(self.pontos):
            range_x = fabs(self.pontos[i + 2].x - self.pontos[i + 1].x)
            range_y = fabs(self.pontos[i + 2].y - self.pontos[i + 1].y)

            if range_x > range_y:
                step = 1.0/range_x
            else:
                step = 1.0/range_y

            j = 0
            while j <= 1:
                _x = ((-1 * pow(j, 3) + 3 * pow(j, 2) - 3 * j + 1) * self.pontos[i].x + \
                     (3 * pow(j, 3) - 6 * pow(j, 2) + 0 * j + 4) * self.pontos[i + 1].x + \
                     (-3 * pow(j, 3) + 3 * pow(j, 2) + 3 * j + 1) * self.pontos[i + 2].x + \
                     (1 * pow(j, 3) + 0 * pow(j, 2) + 0 * j + 0) * self.pontos[i + 3].x) / 6

                _y = ((-1 * pow(j, 3) + 3 * pow(j, 2) - 3 * j + 1) * self.pontos[i].y + \
                      (3 * pow(j, 3) - 6 * pow(j, 2) + 0 * j + 4) * self.pontos[i + 1].y + \
                      (-3 * pow(j, 3) + 3 * pow(j, 2) + 3 * j + 1) * self.pontos[i + 2].y + \
                      (1 * pow(j, 3) + 0 * pow(j, 2) + 0 * j + 0) * self.pontos[i + 3].y) / 6

                p = Ponto(_x, _y)
                pontos_convertidos.append(p)

                j += step

            i += 1

        return pontos_convertidos
