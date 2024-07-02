import networkx as nx

from UI import view
from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni = DAO.getAnni()
        self.stati = DAO.getAllState()
        self.archi = DAO.getArco()
        self.grafo = nx.Graph()

    def buildGraph(self,anno,forma):

        for stato in self.stati:
            self.grafo.add_node(stato)
        for arco in self.archi:
            self.grafo.add_edge(arco[0],arco[1],weight=0)

        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2:
                    if self.grafo.has_edge(nodo1, nodo2):
                        peso = DAO.getPeso(nodo1,nodo2,anno,forma)[0]
                        self.grafo[nodo1][nodo2]["weight"]= peso
        return self.grafo

    def analizza(self):
        diz={}
        for nodo1 in self.grafo.nodes:
            somma = 0
            for nodo2 in self.grafo.nodes:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1,nodo2):
                    peso = self.grafo[nodo1][nodo2]["weight"]
                    somma +=peso
            diz[nodo1] = somma
        return diz




