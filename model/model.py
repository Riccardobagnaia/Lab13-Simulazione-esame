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

        for nodo1 in self.grafo.nodes:
            for nodo2 in self.grafo.nodes:
                if nodo1 != nodo2:
                    arco = DAO.getArco(nodo1,nodo2)
                    if arco[0] is not None:
                        self.grafo.add_edge(nodo1,nodo2)
        return self.grafo

    def listaStati(self):
        stati = []
        for stato in self.grafo.nodes:
            stati.append(stato)
        return stati

    def analizza(self,stato_sel):
        successori = self.grafo.successors(stato_sel)
        predecessori = self.grafo.predecessors(stato_sel)
        raggiungibili = nx.bfs_tree(self.grafo,stato_sel)

        return successori, predecessori ,raggiungibili



