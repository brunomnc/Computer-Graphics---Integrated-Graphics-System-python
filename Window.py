from Ponto import Ponto

class Window(object):
    def __init__(self, minimo_x, minimo_y, maximo_x, maximo_y):
        self.min = Ponto(minimo_x, minimo_y, "ponto minimo")
        self.max = Ponto(maximo_x, maximo_y, "ponto maximo")

    def setCoordenadasMinimo(self, x, y):
        self.min.x = x
        self.min.y = y


    def setCoordenadasMaximo(self, x, y):
        self.max.x = x
        self.max.y = y

    def getXMin(self):
        return self.min.x

    def getXMax(self):
        return self.max.x

    def getYMin(self):
        return self.min.y

    def getYMax(self):
        return self.max.y