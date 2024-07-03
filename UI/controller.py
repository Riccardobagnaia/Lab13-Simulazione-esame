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



    def fillDDanni(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddanno.options.append(ft.dropdown.Option(anno))
        self._view.update_page()


    def avvistamenti(self,e):
        anno = self._view.ddanno.value
        numero = self._model.numAvvistamenti(anno)
        self._view.txt_anno.controls.append(ft.Text(f"{numero[0]}"))
        self._view.update_page()


    def handleGraph(self,e):
        anno = self._view.ddanno.value
        grafo = self._model.buildGraph(anno)
        self.fillDD()
        print(grafo)

    def fillDD(self):
        lista = self._model.listaStati()
        for stato in lista:
            self._view.ddstato.options.append(ft.dropdown.Option(stato))
        self._view.update_page()

    def analizza(self,e):
        stato_sel = self._view.ddstato.value
        succ , prede , adiacenti =self._model.analizza(stato_sel)
        self._view.txt_result.controls.append(ft.Text(f"STATI PRECEDENTI A {stato_sel}"))
        for stato in prede:
            self._view.txt_result.controls.append(ft.Text(f"{stato}"))
        self._view.txt_result.controls.append(ft.Text(f"STATI SUCCESSORI A {stato_sel}"))
        for stato in succ:
            self._view.txt_result.controls.append(ft.Text(f"{stato}"))
        self._view.txt_result.controls.append(ft.Text(f"STATI ADIACENTI A {stato_sel}"))
        for stato in adiacenti:
            self._view.txt_result.controls.append(ft.Text(f"{stato}"))
        self._view.update_page()


