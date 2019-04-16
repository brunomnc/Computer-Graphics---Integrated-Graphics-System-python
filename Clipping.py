import Window as Window
from copy import deepcopy


class Clipping:
    def __init__(self, tela: Window):
        self.inside = 0
        self.left = 1
        self.right = 2
        self.bottom = 4
        self.top = 8

        self.tela = tela

        temp = tela.getXMax() - tela.getXMin()
        aux = (temp - 500) / 10
        self.aux = aux + 50

    def clipping_ponto(self, x, y):
        if x > self.tela.getXMax() - self.aux or self.tela.getXMin() + self.aux or y > self.tela.getYMax() - self.aux or y < self.tela.getYMin() + self.aux:
            return True
        else:
            return False

    def liang_barsky_clipping(self, reta):
        pontos = []
        x_min = self.tela.getXMin() + self.aux
        x_max = self.tela.getXMax() - self.aux
        y_min = self.tela.getYMin() + self.aux
        y_max = self.tela.getYMax() - self.aux

        u1 = 0.0
        u2 = 1.0
        dx = reta.x2 - reta.x1
        dy = reta.y2 - reta.y1
        p = 0.0
        q = 0.0
        r = 0.0
        draw = True

        edge = 0
        while edge < 4:
            if edge == 0:
                p = -dx
                q = reta.x1 - x_min

            if edge == 1:
                p = dx
                q = x_max - reta.x1

            if edge == 2:
                p = -dy
                q = reta.y1 - y_min

            if edge == 3:
                p = dy
                q = y_max - reta.y1

            if p == 0:
                p = 1

            r = q / p

            if p == 0 and q < 0:
                draw = False

            if p < 0:
                if r > u2:
                    draw = False
                if r > u1:
                    u1 = r

            if p > 0:
                if r < u1:
                    draw = False
                if r < u2:
                    u2 = r
            edge += 1

        if draw:
            x1 = reta.x1 + u1 * dx
            y1 = reta.y1 + u1 * dy
            x2 = reta.x1 + u2 * dx
            y2 = reta.y1 + u2 * dy

        pontos.append(x1)
        pontos.append(y1)
        pontos.append(x2)
        pontos.append(y2)

        return pontos

    def sutherland_hodgman_clipping(self, poligono):
        pontos = deepcopy(poligono.pontos)

    def clip_left(self, pontos):
        pass

    def clip_right(self, pontos):
        pass

    def clip_top(self, pontos):
        pass

    def clip_bottom(selfs, pontos):
        pass
