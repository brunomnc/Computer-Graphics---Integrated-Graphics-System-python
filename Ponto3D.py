

class Ponto3D:
    def __init__(self, _x, _y, _z, _nome=None, selected=False):
        self.x = _x
        self.y = _y
        self.z = _z
        self.nome = _nome
        self.selecionado = selected

    def get_attributes(self):
        return str(self), self.nome

    def __str__(self):
        return 'Ponto'

    def get_centro_gravidade(self):
        return self.x, self.y, self.z


