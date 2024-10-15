class GrafoDistancias:
    def __init__(self):
        self.grafo = {}

    def adicionar_distancia(self, origem, destino, distancia):
        if origem not in self.grafo:
            self.grafo[origem] = {}
        self.grafo[origem][destino] = distancia

    def obter_distancia(self, origem, destino):
        return self.grafo.get(origem, {}).get(destino)
