from Ponto import Ponto
from Reta import Reta
from Poligono import Poligono


class Arquivo:

    def __init__(self, nome_arquivo, *objetos:None):
        self.nome_arquivo = nome_arquivo
        self.extensao = '.obj'

        self.objetos_ponto = []
        self.objetos_reta = []
        self.objetos_poligono = []

        for obj in objetos:
            if str(obj[0]) == 'Ponto':
                self.objetos_ponto = obj
            if str(obj[0]) == 'Reta':
                self.objetos_reta = obj
            if str(obj[0]) == 'Poligono':
                self.objetos_poligono = obj

    def salvar(self):
        file = open(self.nome_arquivo + self.extensao, 'w+')

        for p in self.objetos_ponto:
            file.write("o " + p.nome + "\n")
            file.write("v " + str(p.x) + " " + str(p.y) + "\n")

        for r in self.objetos_reta:
            file.write("o " + r.nome + "\n")
            file.write("v " + str(r.x1) + " " + str(r.y1) + "\n")
            file.write("v " + str(r.x2) + " " + str(r.y2) + "\n")

        for y in self.objetos_poligono:
            file.write("o " + y.nome + "\n")
            for s in y.pontos:
                file.write("v " + str(s.x) + " " + str(s.y) + "\n")
                file.write("v " + str(s.x) + " " + str(s.y) + "\n")

        file.close()

    def abrir(self):
        lista_poligonos = []
        lista_pontos = []
        lista_retas = []
        _temp = []

        lista_pontos_poligono = []
        file = open(self.nome_arquivo + self.extensao, 'r')
        conteudo = file.readlines()
        for linha in conteudo:
            if linha[0] == 'o':
                lista_pontos_poligono = []
                nome = str(linha.split()[1])
                poligono = Poligono(lista_pontos_poligono, nome)
                _temp.append(poligono)
            else:
                array_linha = linha.split()
                x = float(array_linha[1])
                y = float(array_linha[2])
                ponto = Ponto(x, y)
                lista_pontos_poligono.append(ponto)
                poligono.pontos = lista_pontos_poligono

        file.close()

        for p in _temp:
            if str(p) == 'Ponto':
                ponto = Ponto(p.pontos[0].x, p.pontos[0].y, p.nome)
                lista_pontos.append(ponto)
            if str(p) == 'Reta':
                reta = Reta(p.pontos[0].x, p.pontos[0].y, p.pontos[1].x, p.pontos[1].y, p.nome)
                lista_retas.append(reta)
            if str(p) == 'Poligono':
                lista_poligonos.append(p)

        lista_objetos = [lista_pontos, lista_retas, lista_poligonos]

        return lista_objetos



