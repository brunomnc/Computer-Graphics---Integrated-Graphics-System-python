from Ponto import Ponto
from Ponto3D import Ponto3D
from numpy import array, append


class Objeto3D:
    def __init__(self, _segmentos: [[Ponto3D, Ponto3D]], _nome: str = None, selected=False):
        self.segmentos = _segmentos
        self.nome = _nome
        self.selecionado = selected

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
        if len(self.segmentos) == 1:
            return 'Reta3D'
        return 'Objeto3D'

    def at(self, index: int):
        return self.segmentos[index]

    def get_centro_gravidade(self):
        x = 0
        y = 0
        z = 0
        for segmento in self.segmentos:
            x += (segmento[0].x + segmento[1].x)/2
            y += (segmento[0].y + segmento[1].y)/2
            z += (segmento[0].z + segmento[1].z)/2

        return x / len(self.segmentos), y / len(self.segmentos), z / len(self.segmentos)

    def __eq__(self, other):
        if self.nome == other.nome:
            return True
        else:
            return False