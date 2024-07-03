import networkx as nx

from UI import view
from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni = DAO.getAnni()
        self.grafo = nx.DiGraph()

    def getAnni(self):
        return self.anni

    def numAvvistamenti(self,anno):
        numero = DAO.getAvvistamenti(anno)
        return numero

    def buildGraph(self,anno):
        nodi = DAO.getNodi(anno)
        for stato in nodi:
            self.grafo.add_node(stato)
        return self.grafo




