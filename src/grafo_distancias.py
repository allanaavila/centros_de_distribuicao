import csv
import heapq


class GrafoDistancia:
    def __init__(self):
        self.cidades = {}

    def adicionarCidade(self, nomeCidade):
        if nomeCidade not in self.cidades:
            self.cidades[nomeCidade] = {}

    def adicionarRota(self, cidade1, cidade2, distancia):
        if cidade1 in self.cidades and cidade2 in self.cidades:
            self.cidades[cidade1][cidade2] = distancia
            self.cidades[cidade2][cidade1] = distancia

    def encontrarRotaMaisCurta(self, origem, destino):
        distancias = {cidade: float('inf') for cidade in self.cidades}
        distancias[origem] = 0
        caminho = {cidade: None for cidade in self.cidades}

        fila = [(0, origem)]

        while fila:
            distancia_atual, cidade_atual = heapq.heappop(fila)

            if cidade_atual == destino:
                break

            for vizinho, distancia in self.cidades[cidade_atual].items():
                nova_distancia = distancia_atual + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    caminho[vizinho] = cidade_atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        rota = []
        cidade = destino
        while cidade:
            rota.append(cidade)
            cidade = caminho[cidade]
        rota.reverse()

        return rota, distancias[destino] if distancias[destino] != float('inf') else None

    def atualizarDistancias(self, novasRotas):
        for cidade1, cidade2, distancia in novasRotas:
            self.adicionarCidade(cidade1)
            self.adicionarCidade(cidade2)
            self.adicionarRota(cidade1, cidade2, distancia)

        self.salvarDistancias()

    def salvarDistancias(self):
        with open('data/distancias.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['origem', 'destino', 'distancia'])
            writer.writeheader()
            for cidade1 in self.cidades:
                for cidade2, distancia in self.cidades[cidade1].items():
                    if cidade1 < cidade2:
                        writer.writerow({'origem': cidade1, 'destino': cidade2, 'distancia': distancia})
