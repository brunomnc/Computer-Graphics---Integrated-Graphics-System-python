import array
import Ponto

class Poligono(object):
    def __init__(self, _pontos:array, _nome:str):
        self.pontos = _pontos
        self.nome = _nome

    def get_pontos(self):
        return self.pontos

    def get_nome(self):
        return self.nome

