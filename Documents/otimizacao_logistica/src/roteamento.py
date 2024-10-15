import logging
from src.caminhao import Caminhao
from src.entrega import Entrega
from src.grafo_distancias import GrafoDistancia

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Roteamento:
    def __init__(self, grafo: GrafoDistancia, caminhões: list):
        self.grafo = grafo
        self.caminhões = caminhões
        self.entregas = []

    def adicionar_entrega(self, entrega: Entrega):
        if entrega.carga < 0:
            raise ValueError("Carga não pode ser negativa.")
        self.entregas.append(entrega)

    def alocar_entregas(self):
        self.entregas.sort(key=lambda e: e.prazo)

        for entrega in self.entregas:
            alocado = False
            melhor_distancia = float('inf')
            melhor_caminhao = None
            melhor_rota = []

            for caminhao in self.caminhões:
                if caminhao.isDisponivel() and caminhao.cargaAtual + entrega.carga <= caminhao.capacidade:
                    rota, distancia = self.grafo.encontrarRotaMaisCurta(caminhao.localizacaoAtual, entrega.destino)
                    if distancia is not None and distancia < melhor_distancia:
                        melhor_distancia = distancia
                        melhor_caminhao = caminhao
                        melhor_rota = rota

            if melhor_caminhao:
                sucesso = melhor_caminhao.carregarEntrega(entrega.carga)
                if sucesso:
                    self._atualizar_caminhao(melhor_caminhao, entrega.destino)
                    alocado = True
                    logging.info(f"Entrega {entrega.idEntrega} alocada ao caminhão {melhor_caminhao.idCaminhao}.")
                    logging.info(f"Rota: {' -> '.join(melhor_rota)} | Distância: {melhor_distancia} km")
                else:
                    logging.warning(f"Caminhão {melhor_caminhao.idCaminhao} não conseguiu carregar a entrega {entrega.idEntrega}.")

            if not alocado:
                logging.error(f"Entrega {entrega.idEntrega} não pôde ser alocada a nenhum caminhão disponível.")

    def _atualizar_caminhao(self, caminhao, novo_destino):
        caminhao.disponivel = False
        caminhao.atualizarLocalizacao(novo_destino)