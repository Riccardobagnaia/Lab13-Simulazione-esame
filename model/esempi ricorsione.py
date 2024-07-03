# def ricorsione(self, parziale):
#     if self.puoEssereSol(parziale):  #ho raggiunto condizione terminale: non ho piu vicini validi da inserire
#         if self.soluzioneMigliore(parziale):  #controllo se è la migliore
#             self.bestPath = copy.deepcopy(parziale)  #copio
#             self.bestScore = self.calcolaPeso(parziale)  #salvo il peso
#         return  #vado alla pop per scrivere un'altra soluzione
#     for n in self.grafo.neighbors(parziale[-1]):  #il prossimo deve essere collegato all'ultimo del parziale (è un cammimo)
#         if self.nodoValido(parziale,n):  #controllo se il nodo rispetta i vincoli
#             parziale.append(n)  #aggiunto
#             self.ricorsione(parziale)  #richiamo
#             parziale.pop()  #vado qui dopo le return


#**********ricorsione ufo *************

# def getPath(self):
#     # caching con variabili della classe (percorso migliore e peso maggiore)
#     self._bestComp = []
#     self._bestdTot = 0
#     # inizializzo il parziale con il nodo iniziale
#     parziale = []
#
#     for a in self.grafo.nodes:
#         if a not in parziale:
#             parziale.append(a)
#             self._ricorsionev2(parziale)
#             parziale.pop()  # rimuovo l'ultimo elemento aggiunto: backtracking
#     return self._bestComp, self._bestdTot
#
#
# def _ricorsionev2(self, parziale):
#     # verifico se soluzione è migliore di quella salvata in cache
#
#     if self.getScore(parziale) > self._bestdTot:
#         # se lo è aggiorno i valori migliori
#         self._bestComp = copy.deepcopy(parziale)
#         self._bestdTot = self.getScore(parziale)
#     # verifico se posso aggiungere un altro elemento
#     comp = self.grafo.neighbors(parziale[-1])
#     for a in comp:
#         if a not in parziale:
#             if len(parziale) < 2:
#                 parziale.append(a)
#                 self._ricorsionev2(parziale)
#                 parziale.pop()
#             elif self.grafo[parziale[-1]][a]["weight"] > self.grafo[parziale[-2]][parziale[-1]]["weight"]:
#                 parziale.append(a)
#                 self._ricorsionev2(parziale)
#                 parziale.pop()  # rimuovo l'ultimo elemento aggiunto: backtracking
#
#
# def getScore(self, list):
#     score = 0
#     for i in range(0, len(list) - 1):
#         score += distance.geodesic((list[i].Lat, list[i].Lng), (list[i + 1].Lat, list[i + 1].Lng)).km
#     return score

# NEL CONTROLLER *********
# def handle_path(self, e):
#     cammino = self._model.getPath()
#     self._view.txtOut2.controls.append(
#         ft.Text(f"Peso cammino massimo :{cammino[1]}"))
#     self._view.update_page()
#     for i in range(0, len(cammino[0]) - 1):
#         self._view.txtOut2.controls.append(
#             ft.Text(
#                 f"{cammino[0][i].id}-->{cammino[0][i + 1].id}, peso: {self._model.grafo[cammino[0][i]][cammino[0][i + 1]]["weight"]}, distance: {distance.distance((cammino[0][i].Lat, cammino[0][i].Lng), (cammino[0][i + 1].Lat, cammino[0][i + 1].Lng))}"))
#         self._view.update_page()