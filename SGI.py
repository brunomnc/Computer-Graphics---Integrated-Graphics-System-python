import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import array
from Ponto import Ponto
import Reta
import Poligono

listaPontos = []
listaRetas = []
listaPoligonos = []

surface = None

MainWindow = None
store = Gtk.ListStore(str, str, float)


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

def desenhaPonto(ponto):
    ctx = cairo.Context(surface)
    # ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(5)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(ponto.x, ponto.y)
    ctx.line_to(ponto.x, ponto.y)
    ctx.stroke()
    ctx.save()

def clear_surface():
    cr = cairo.Context(surface)
    cr.set_source_rgb(1,1,1)
    cr.paint()

    del cr


def configure_event_cb(wid,evt):
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

def draw_cb(wid,cr):
    global surface

    cr.set_source_surface(surface,0,0)
    cr.paint()
    return False

# carregando interface Glade
class MainWindow(Gtk.Window):

    def __init__(self):

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
        self.objectsListStore = Gtk.ListStore(str, str, float)
        self.objectsCellRenderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Nome", self.objectsCellRenderer, text=0)
        column = Gtk.TreeViewColumn("Tipo", self.objectsCellRenderer, text=0)
        self.objectTreeView.append_column(column)


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

        self.btnPonto.connect("clicked", self.onBtnPontoClicked)
        self.btnSalvarPonto.connect("clicked", self.onBtnSalvarPontoClicked)
        self.btnCancelaPonto.connect("clicked", self.onBtnCancelaPontoClicked)

        self.DrawingFrame.connect('draw', draw_cb)
        self.DrawingFrame.connect('configure-event', configure_event_cb)

        builder.connect_signals(Handler())

        # exibe tela inicial SGI
        MainWindow.show_all()
        Gtk.main()

    def onBtnPontoClicked(self, button):
        self.PontoWindow.show_all()

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

    def onBtnRetaClicked(self, button):
        self.RetaWindow.show_all()

    def onBtnPoligonoClicked(self, button):
        self.PoligonoWindow.show_all()





win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



