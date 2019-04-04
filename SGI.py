import cairo
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib
import array
from Ponto import Ponto
from Window import Window
from Reta import Reta
from Poligono import Poligono

listaPontos = []
listaRetas = []
listaPoligonos = []
lista_ponto_poligono = []

xViewPortMax = 500
xViewPortMin = 0
yViewPortMax = 500
yViewPortMin = 0

surface = None
widget = None

DrawingFrame = None
MainWindow = None
store = Gtk.ListStore(str, str)

tela = Window(xViewPortMin, yViewPortMin, xViewPortMax, yViewPortMax)


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()


def transformadaViewPortCoordenadaX(x):
    auxiliar = (x - tela.getXMin()) / (tela.getXMax() - tela.getXMin())

    return auxiliar * (xViewPortMax - xViewPortMin)


def transformadaViewPortCoordenadaY(y):
    auxiliar = (y - tela.getYMin()) / (tela.getYMax() - tela.getYMin())

    return (1 - auxiliar) * (yViewPortMax - yViewPortMin)


def atualizarTela():
    clear_surface()
    redesenha_pontos()
    redesenha_retas()
    redesenha_poligonos()
    # atualiza widget do DrawingFrame
    widget.queue_draw()


def redesenha_pontos():
    for ponto in listaPontos:
        desenhaPonto(ponto)


def redesenha_retas():
    for reta in listaRetas:
        desenhaReta(reta)


def redesenha_poligonos():
    for poligono in listaPoligonos:
        desenha_poligono(poligono)


def desenhaPonto(ponto):
    ctx = cairo.Context(surface)
    ctx.save()
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(transformadaViewPortCoordenadaX(ponto.x), transformadaViewPortCoordenadaY(ponto.y))
    ctx.line_to(transformadaViewPortCoordenadaX(ponto.x), transformadaViewPortCoordenadaY(ponto.y))
    ctx.stroke()
    ctx.restore()


def desenhaReta(reta):
    ctx = cairo.Context(surface)
    ctx.save()
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(transformadaViewPortCoordenadaX(reta.x1), transformadaViewPortCoordenadaY(reta.y1))
    ctx.line_to(transformadaViewPortCoordenadaX(reta.x2), transformadaViewPortCoordenadaY(reta.y2))
    ctx.stroke()
    ctx.restore()


def desenha_poligono(poligono):
    _ponto = poligono.at(0)

    ctx = cairo.Context(surface)
    ctx.save()
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(transformadaViewPortCoordenadaX(_ponto.x), transformadaViewPortCoordenadaY(_ponto.y))

    for p in poligono.pontos:
        ctx.line_to(transformadaViewPortCoordenadaX(p.x), transformadaViewPortCoordenadaY(p.y))

    ctx.line_to(transformadaViewPortCoordenadaX(_ponto.x), transformadaViewPortCoordenadaY(_ponto.y))

    ctx.stroke()
    ctx.restore()


def clear_surface():
    cr = cairo.Context(surface)
    cr.set_source_rgb(1, 1, 1)
    cr.paint()

    del cr


def configure_event_cb(wid, evt):
    global surface

    if surface is not None:
        del surface
        surface = None

    win = wid.get_window()
    width = wid.get_allocated_width()
    height = wid.get_allocated_height()

    surface = win.create_similar_surface(
        cairo.CONTENT_COLOR,
        width,
        height)

    clear_surface()
    return True


def draw_cb(wid, cr):
    global surface
    global widget
    widget = wid

    cr.set_source_surface(surface, 0, 0)
    cr.paint()
    return False


# carregando interface Glade
class MainWindow(Gtk.Window):

    def __init__(self):
        p = Ponto(50, 50, 'q')
        q = Ponto(10, 10, 'r')

        listaPontos.append(p)
        listaPontos.append(q)

        poly = Poligono([p, q], 's')
        listaPoligonos.append(poly)

        builder = Gtk.Builder()
        builder.add_from_file("view.glade")

        # carregando elementos
        MainWindow = builder.get_object("MainWindow")

        self.PontoWindow = builder.get_object("PontoWindow")
        self.RetaWindow = builder.get_object("RetaWindow")
        self.PoligonoWindow = builder.get_object("PoligonoWindow")
        self.ExclusaoWindow = builder.get_object("ExclusaoWindow")
        self.AlertaWindow = builder.get_object("AlertaWindow")
        self.DrawingFrame = builder.get_object("DrawingFrame")

        self.objectTreeView = builder.get_object("objectTreeView")
        self.objectTreeView.set_model(store)

        self.objectsCellRenderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Nome", self.objectsCellRenderer, text=0)
        self.objectTreeView.append_column(column)
        column = Gtk.TreeViewColumn("Tipo", self.objectsCellRenderer, text=1)
        self.objectTreeView.append_column(column)

        self.objectTreeView.get_selection()

        store.append(p.get_attributes())
        store.append(q.get_attributes())
        store.append(poly.get_attributes())

        self.btnPonto = builder.get_object("btnPonto")
        self.btnReta = builder.get_object("btnReta")
        self.btnPoligono = builder.get_object("btnPoligono")
        self.btnUp = builder.get_object("btnUp")
        self.btnDown = builder.get_object("btnDown")
        self.btnLeft = builder.get_object("btnLeft")
        self.btnRight = builder.get_object("btnRight")
        self.btnZoomIn = builder.get_object("btnZoomIn")
        self.btnZoomOut = builder.get_object("btnZoomOut")
        self.btnLimpaTela = builder.get_object("btnLimpaTela")
        self.btnRotacionarDireita = builder.get_object("btnRotacionarDireita")
        self.btnRotacionarEsquerda = builder.get_object("btnRotacionarEsquerda")
        self.btnDeletaItem = builder.get_object("btnDeletaItem")

        self.btnSalvarPonto = builder.get_object("btnSalvarPonto")
        self.btnCancelaPonto = builder.get_object("btnCancelaPonto")
        self.btnSpinX = builder.get_object("btnSpinX")
        self.btnSpinY = builder.get_object("btnSpinY")
        self.textFieldNome = builder.get_object("textFieldNome")

        self.btnSalvarReta = builder.get_object("btnSalvarReta")
        self.btnCancelarReta = builder.get_object("btnCancelarReta")
        self.spinRetaX1 = builder.get_object("spinRetaX1")
        self.spinRetaY1 = builder.get_object("spinRetaY1")
        self.spinRetaX2 = builder.get_object("spinRetaX2")
        self.spinRetaY2 = builder.get_object("spinRetaY2")
        self.textFieldRetaNome = builder.get_object("textFieldRetaNome")

        self.btnConfirmaExclusao = builder.get_object("btnConfirmaExclusao")
        self.btnCancelaExclusao = builder.get_object("btnCancelaExclusao")

        self.poligonoX = builder.get_object("poligonoX")
        self.poligonoY = builder.get_object("poligonoY")
        self.poligonoZ = builder.get_object("poligonoZ")
        self.btnSalvarPoligono = builder.get_object("btnSalvarPoligono")
        self.btnCancelarPoligono = builder.get_object("btnCancelarPoligono")
        self.textFieldPoligonoName = builder.get_object("textFieldPoligonoName")
        self.btnAdicionaPontoPoligono = builder.get_object("btnAdicionaPontoPoligono")

        self.btnWindowAlerta = builder.get_object("btnWindowAlerta")
        self.mensagemTituloAviso = builder.get_object("mensagemTituloAviso")
        self.mensagemAviso = builder.get_object("mensagemAviso")

        # acao click de janelas Ponto
        self.btnPonto.connect("clicked", self.onBtnPontoClicked)
        self.btnSalvarPonto.connect("clicked", self.onBtnSalvarPontoClicked)
        self.btnCancelaPonto.connect("clicked", self.onBtnCancelaPontoClicked)

        # acao click de janelas Reta
        self.btnReta.connect("clicked", self.onBtnRetaClicked)
        self.btnSalvarReta.connect("clicked", self.onBtnSalvarRetaClicked)
        self.btnCancelarReta.connect("clicked", self.onBtnCancelaRetaClicked)

        # acao click janela Poligono
        self.btnPoligono.connect("clicked", self.onBtnPoligonoClicked)
        self.btnAdicionaPontoPoligono.connect("clicked", self.onBtnAdicionaPontoPoligonoClicked)
        self.btnSalvarPoligono.connect("clicked", self.onBtnSalvarPoligonoClicked)
        self.btnCancelarPoligono.connect("clicked", self.onBtnCancelaPoligonoClicked)

        # acao click janela
        self.btnDown.connect("clicked", self.onBtnDownClicked)
        self.btnUp.connect("clicked", self.onBtnUpClicked)
        self.btnLeft.connect("clicked", self.onBtnLeftClicked)
        self.btnRight.connect("clicked", self.onBtnRightClicked)

        self.btnZoomIn.connect("clicked", self.onBtnZoomInClicked)
        self.btnZoomOut.connect("clicked", self.onBtnZoomOutClicked)

        self.DrawingFrame.connect('draw', draw_cb)
        self.DrawingFrame.connect('configure-event', configure_event_cb)

        builder.connect_signals(Handler())

        # exibe tela inicial SGI
        MainWindow.show_all()
        Gtk.main()

    def onBtnPontoClicked(self, button):
        self.PontoWindow.show_all()

    def onBtnRetaClicked(self, button):
        self.RetaWindow.show_all()

    def onBtnSalvarPontoClicked(self, button):
        x = self.btnSpinX.get_value_as_int()
        y = self.btnSpinY.get_value_as_int()
        nome = self.textFieldNome.get_text()

        ponto = Ponto(x, y, nome)
        listaPontos.append(ponto)
        desenhaPonto(ponto)
        self.PontoWindow.hide()

    def onBtnCancelaPontoClicked(self, button):
        self.PontoWindow.hide()

    def onBtnSalvarRetaClicked(self, button):
        print('teste')
        x1 = self.spinRetaX1.get_value_as_int()
        y1 = self.spinRetaY1.get_value_as_int()
        x2 = self.spinRetaX2.get_value_as_int()
        y2 = self.spinRetaY2.get_value_as_int()
        nome = self.textFieldRetaNome.get_text()
        reta = Reta(x1, y1, x2, y2, nome)
        listaRetas.append(reta)
        desenhaReta(reta)
        self.RetaWindow.hide()

    def onBtnCancelaRetaClicked(self, button):
        self.RetaWindow.hide()

    def onBtnPoligonoClicked(self, button):
        self.PoligonoWindow.show_all()

    def onBtnAdicionaPontoPoligonoClicked(self, button):
        x = self.poligonoX.get_value_as_int()
        y = self.poligonoY.get_value_as_int()
        p = Ponto(x, y)
        lista_ponto_poligono.append(p)

    def onBtnSalvarPoligonoClicked(self, button):
        nome = self.textFieldPoligonoName.get_text()
        pontos = lista_ponto_poligono
        poligono = Poligono(pontos, nome)
        listaPoligonos.append(poligono)
        desenha_poligono(poligono)
        self.PoligonoWindow.hide()
        lista_ponto_poligono.clear()

    def onBtnCancelaPoligonoClicked(self, button):
        self.PoligonoWindow.hide()

    def onBtnDownClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        yMaximo -= 10
        yMinimo -= 10

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()

    def onBtnUpClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        yMaximo += 10
        yMinimo += 10

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()

    def onBtnLeftClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        xMaximo -= 10
        xMinimo -= 10

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()

    def onBtnRightClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        xMaximo += 10
        xMinimo += 10

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()

    def onBtnZoomInClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        xMaximo -= 5
        xMinimo += 5
        yMaximo -= 5
        yMinimo += 5

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()

    def onBtnZoomOutClicked(self, button):
        xMaximo = tela.getXMax()
        xMinimo = tela.getXMin()
        yMaximo = tela.getYMax()
        yMinimo = tela.getYMin()

        xMaximo += 5
        xMinimo -= 5
        yMaximo += 5
        yMinimo -= 5

        tela.setCoordenadasMaximo(xMaximo, yMaximo)
        tela.setCoordenadasMinimo(xMinimo, yMinimo)

        atualizarTela()


class Operacoes:
    def __init__(self):
        self.lista_pontos = []
        self.lista_retas = []
        self.lista_poligonos = []
        self.lista_ponto_poligono = []

    def transformadaViewPortCoordenadaX(x):
        auxiliar = (x - tela.getXMin()) / (tela.getXMax() - tela.getXMin())

        return auxiliar * (xViewPortMax - xViewPortMin)

    def transformadaViewPortCoordenadaY(y):
        auxiliar = (y - tela.getYMin()) / (tela.getYMax() - tela.getYMin())

        return (1 - auxiliar) * (yViewPortMax - yViewPortMin)

    def atualizarTela(self):
        clear_surface()
        redesenha_pontos()
        redesenha_retas()
        redesenha_poligonos()
        # atualiza widget do DrawingFrame
        widget.queue_draw()

    def redesenha_pontos(self):
        for ponto in listaPontos:
            desenhaPonto(ponto)

    def redesenha_retas(self):
        for reta in listaRetas:
            desenhaReta(reta)

    def redesenha_poligonos(self):
        for poligono in listaPoligonos:
            desenha_poligono(poligono)

    def desenhaPonto(self, ponto):
        ctx = cairo.Context(surface)
        ctx.save()
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(transformadaViewPortCoordenadaX(ponto.x), transformadaViewPortCoordenadaY(ponto.y))
        ctx.line_to(transformadaViewPortCoordenadaX(ponto.x), transformadaViewPortCoordenadaY(ponto.y))
        ctx.stroke()
        ctx.restore()

    def desenhaReta(self, reta):
        ctx = cairo.Context(surface)
        ctx.save()
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(transformadaViewPortCoordenadaX(reta.x1), transformadaViewPortCoordenadaY(reta.y1))
        ctx.line_to(transformadaViewPortCoordenadaX(reta.x2), transformadaViewPortCoordenadaY(reta.y2))
        ctx.stroke()
        ctx.restore()

    def desenha_poligono(self, poligono):
        _ponto = poligono.at(0)

        ctx = cairo.Context(surface)
        ctx.save()
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(transformadaViewPortCoordenadaX(_ponto.x), transformadaViewPortCoordenadaY(_ponto.y))

        for p in poligono.pontos:
            ctx.line_to(transformadaViewPortCoordenadaX(p.x), transformadaViewPortCoordenadaY(p.y))

        ctx.line_to(transformadaViewPortCoordenadaX(_ponto.x), transformadaViewPortCoordenadaY(_ponto.y))

        ctx.stroke()
        ctx.restore()


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
