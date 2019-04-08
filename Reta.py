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

    def get_centro_gravidade(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def __eq__(self, other):
        if self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2 and self.nome == other.nome:
            return True
        else:
            return False
