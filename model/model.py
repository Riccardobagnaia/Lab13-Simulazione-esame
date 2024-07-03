import networkx as nx

from UI import view
from database.DAO import DAO


class Model:
    def __init__(self):
        self.stati = DAO.getStati()
        self.grafo = nx.Graph()
        self.archi = DAO.getArchi()


    def buildGraph(self,data,xG):
        for stato in self.stati:
            self.grafo.add_node(stato)
        for arco in self.archi:
            peso = DAO.getPeso(arco[0],arco[1],data,xG)[0]
            self.grafo.add_edge(arco[0],arco[1],weight=peso)

        return self.grafo

    def adiacenti(self):
        diz = {}
        for stato in self.grafo.nodes:
            somma = 0
            for stato2 in self.grafo.nodes:
                if self.grafo.has_edge(stato,stato2):
                    peso = self.grafo[stato][stato2]["weight"]
                    somma += peso
            diz[stato] = somma
        return diz







