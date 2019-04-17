import Window as Window
from copy import deepcopy
from Ponto import Ponto


class Clipping:
    def __init__(self, tela: Window):
        self.INSIDE = 0
        self.LEFT = 1
        self.RIGHT = 2
        self.BOTTOM = 4
        self.TOP = 8

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
        _left = self.clip_left(pontos)
        _right = self.clip_right(_left)
        _top = self.clip_top(_right)
        _bottom = self.clip_bottom(_top)

        return _bottom

    def clip_left(self, pontos):
        clip_x = self.tela.getXMin() + self.aux
        output = []

        if len(pontos) == 0:
            return [];

        pontos.append(pontos[0])
        sz = len(pontos) - 1
        i = 0
        while i < sz:
            c_0 = pontos[i]
            c_1 = pontos[i+1]

            if c_0.x < clip_x and c_1.x < clip_x:
                pass

            if c_0.x >= clip_x and c_1.x >= clip_x:
                output.append(c_1)

            x = clip_x
            try:
                m = (c_1.y - c_0.y)/(c_1.x - c_0.x)
            except:
                m = 1

            y = m * (x - c_0.x) + c_0.y

            if c_0.x >= clip_x and c_1.x < clip_x:
                p = Ponto(x, y)
                output.append(p)

            if c_0.x < clip_x and c_1.x >= clip_x:
                p = Ponto(x, y)
                output.append(p)
                output.append(c_1)

            i += 1

        return output

    def clip_right(self, pontos):
        clip_x = self.tela.getXMax() - self.aux
        output = []

        if len(pontos) == 0:
            return [];

        pontos.append(pontos[0])
        sz = len(pontos) - 1
        i = 0
        while i < sz:
            c_0 = pontos[i]
            c_1 = pontos[i+1]

            if c_0.x >= clip_x and c_1.x >= clip_x:
                pass

            if c_0.x < clip_x and c_1.x < clip_x:
                output.append(c_1)

            x = clip_x

            try:
                m = (c_1.y - c_0.y)/(c_1.x - c_0.x)
            except:
                m = 1

            y = m * (x - c_0.x) + c_0.y

            if c_0.x < clip_x and c_1.x >= clip_x:
                p = Ponto(x, y)
                output.append(p)

            if c_0.x >= clip_x and c_1.x < clip_x:
                p = Ponto(x, y)
                output.append(p)
                output.append(c_1)

            i += 1

        return output

    def clip_top(self, pontos):
        clip_y = self.tela.getYMax() - self.aux

        if len(pontos) == 0:
            return [];

        output = []
        pontos.append(pontos[0])
        sz = len(pontos) - 1
        i = 0
        while i < sz:
            c_0 = pontos[i]
            c_1 = pontos[i+1]

            if c_0.y > clip_y and c_1.y > clip_y:
                pass

            if c_0.y <= clip_y and c_1.y <= clip_y:
                output.append(c_1)

            y = clip_y
            try:
                m = (c_1.x - c_0.x)/(c_1.y - c_0.y)
            except:
                m=1

            x = m * (y - c_0.y) + c_0.x

            if c_0.y <= clip_y and c_1.y > clip_y:
                p = Ponto(x, y)
                output.append(p)

            if c_0.y > clip_y and c_1.y <= clip_y:
                p = Ponto(x, y)
                output.append(p)
                output.append(c_1)

            i += 1

        return output

    def clip_bottom(self, pontos):
        clip_y = self.tela.getYMin() + self.aux
        output = []

        if len(pontos) == 0:
            return [];

        pontos.append(pontos[0])
        sz = len(pontos) - 1
        i = 0
        while i < sz:
            c_0 = pontos[i]
            c_1 = pontos[i+1]

            if c_0.y < clip_y and c_1.y < clip_y:
                pass

            if c_0.y >= clip_y and c_1.y >= clip_y:
                output.append(c_1)

            y = clip_y
            try:
                m = (c_1.x - c_0.x)/(c_1.y - c_0.y)
            except:
                m=1

            x = m * (y - c_0.y) + c_0.x

            if c_0.y >= clip_y and c_1.y < clip_y:
                p = Ponto(x, y)
                output.append(p)

            if c_0.y < clip_y and c_1.y >= clip_y:
                p = Ponto(x, y)
                output.append(p)
                output.append(c_1)

            i += 1

        return output

    def buscar_codigo(self, x, y):
        x_min = self.tela.getXMin() + self.aux
        x_max = self.tela.getXMax() - self.aux
        y_min = self.tela.getYMin() + self.aux
        y_max = self.tela.getYMax() - self.aux

        code = self.INSIDE

        if x < x_min:
            code |= self.LEFT
        if x > x_max:
            code |= self.RIGHT
        if y < y_min:
            code |= self.BOTTOM
        if y > y_max:
            code |= self.TOP

        return code

    def cohen_sutherland_clipping(self, reta):
        x_min = self.tela.getXMin() + self.aux
        x_max = self.tela.getXMax() - self.aux
        y_min = self.tela.getYMin() + self.aux
        y_max = self.tela.getYMax() - self.aux

        code_0 = self.buscar_codigo(reta.x1, reta.y1)
        code_1 = self.buscar_codigo(reta.x2, reta.y2)

        aceita = False

        while True:
            if not(code_0 | code_1):
                aceita = True
                break

            if code_0 & code_1:
                break

            else:
                x = 0
                y = 0

                _code = None

                if code_0:
                    _code = code_0
                else:
                    _code = code_1

                if _code & self.TOP:
                    x = reta.x1 + (reta.x2 - reta.x1) * (y_max - reta.y1) / (reta.y2 - reta.y1)
                    y = y_max

                if _code & self.BOTTOM:
                    x = reta.x1 + (reta.x2 - reta.x1) * (y_min - reta.y1) / (reta.y2 - reta.y1)
                    y = y_min

                if _code & self.RIGHT:
                    y = reta.y1 + (reta.y2 - reta.y1) * (x_max - reta.x1) / (reta.x2 - reta.x1)
                    x = x_max

                if _code & self.LEFT:
                    y = reta.y1 + (reta.y2 - reta.y1) * (x_min - reta.x1) / (reta.x2 - reta.x1)
                    x = x_min

                if _code == code_0:
                    reta.x1 = x
                    reta.y1 = y

                    code_0 = self.buscar_codigo(reta.x1, reta.y1)
                else:
                    reta.x2 = x
                    reta.y2 = y

                    code_1 = self.buscar_codigo(reta.x2, reta.y2)

        if aceita:
            pontos = []
            pontos.append(reta.x1)
            pontos.append(reta.y1)
            pontos.append(reta.x2)
            pontos.append(reta.y2)

            return pontos
        else:
            return []



