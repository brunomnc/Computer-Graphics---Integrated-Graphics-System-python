from Ponto import Ponto
from typing import List


class Poligono:
    def __init__(self, _pontos: List[Ponto], _nome: str):
        self.pontos = _pontos
        self.nome = _nome

    def get_pontos(self):
        return self.pontos

    def get_nome(self):
        return self.nome
