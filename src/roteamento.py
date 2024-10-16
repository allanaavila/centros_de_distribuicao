from typing import List, Dict
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia
from src.rota import Rota


class Roteamento:
    def __init__(self, grafo: GrafoDistancia, centros: List[CentroDistribuicao]):
        self.grafo = grafo
        self.centros = centros

    def encontrar_centro_mais_proximo(self, destino: str) -> CentroDistribuicao:
        centro_mais_proximo = None
        menor_distancia = float('inf')

        for centro in self.centros:
            distancia = self.grafo.encontrarRotaMaisCurta(centro.cidade, destino)[1]
            if distancia < menor_distancia:
                menor_distancia = distancia
                centro_mais_proximo = centro

        return centro_mais_proximo

    def adicionar_entrega(self, entrega: Entrega, centro: CentroDistribuicao):
        centro.adicionar_entrega(entrega)

    def alocar_entregas(self) -> Dict[CentroDistribuicao, List[Rota]]:
        rotas_por_centro: Dict[CentroDistribuicao, List[Rota]] = {centro: [] for centro in self.centros}

        for centro in self.centros:
            entregas_ordenadas = sorted(centro.entregas, key=lambda e: e.prazo)

            for entrega in entregas_ordenadas:
                rota_alocada = False
                for rota in rotas_por_centro[centro]:
                    if rota.caminhao.pode_adicionar_entrega(entrega):
                        distancia = self.grafo.encontrarRotaMaisCurta(rota.caminhao.localizacaoAtual, entrega.destino)[
                            1]
                        rota.adicionar_entrega(entrega, distancia)
                        rota.caminhao.adicionar_entrega(entrega)
                        rota_alocada = True
                        break

                if not rota_alocada:
                    for caminhao in centro.caminhoes:
                        if caminhao.esta_disponivel() and caminhao.pode_adicionar_entrega(entrega):
                            nova_rota = Rota(caminhao)
                            distancia = self.grafo.encontrarRotaMaisCurta(caminhao.localizacaoAtual, entrega.destino)[1]
                            nova_rota.adicionar_entrega(entrega, distancia)
                            caminhao.adicionar_entrega(entrega)
                            rotas_por_centro[centro].append(nova_rota)
                            break

        return rotas_por_centro