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


    def handle_graph(self,e):
        data = self._view.txt_anno.value
        giorni = self._view.txt_giorni.value
        try:
            dataInt= int(data)
            if dataInt <1906 or dataInt>2014:
                self._view.txt_result.controls.append(ft.Text("Data deve essere compresa tra 1906 e 2014", color="red"))
                self._view.update_page()

            xG = int(giorni)
            if xG<1 or xG >180:
                self._view.txt_result.controls.append(ft.Text("Data deve essere compresa tra 1 e 180", color="red"))
                self._view.update_page()
            grafo = self._model.buildGraph(dataInt, xG)
            self._view.txt_result.controls.append(ft.Text(f"{grafo}"))
            self._view.update_page()

            diz = self._model.adiacenti()
            for chiave in diz:
                self._view.txt_result.controls.append(ft.Text(f"stato {chiave} somma adiacenti: {diz[chiave]}"))
            self._view.update_page()


        except ValueError :
            self._view.txt_result.controls.append(ft.Text("Scrivere dei numeri",color="red"))
            self._view.update_page()

