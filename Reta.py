class Reta:
    def __init__(self, _x1, _y1, _x2, _y2, _nome=None):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2
        self.nome = _nome

    def __str__(self):
        return 'Reta'

    def get_sttributes(self):
        return str(self), self.nome
