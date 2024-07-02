import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = self._model.anni
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(key=anno))
        self._view.update_page()
    def fillForma(self,e):
        anno_sel = self._view.ddyear.value
        print(anno_sel)
        forme = DAO.getForme(anno_sel)
        for forma in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(forma))
        self._view.update_page()

    def handle_graph(self, e):
        anno_sel = self._view.ddyear.value
        forma = self._view.ddshape.value
        if forma is None:
            pass
        grafo = self._model.buildGraph(anno_sel,forma)
        self._view.txt_result.controls.append(ft.Text(f"Grafo con {len(grafo.nodes)} vertici e {len(grafo.edges)} archi"))
        self._view.update_page()
        diz = self._model.analizza()
        for stato in diz:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {stato}, somma pesi {diz[stato]}"))
        self._view.update_page()


    def handle_path(self, e):
        pass