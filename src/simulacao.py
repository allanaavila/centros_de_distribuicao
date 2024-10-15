import logging

from src.caminhao import Caminhao
from src.entrega import Entrega
from src.grafo_distancias import GrafoDistancia
from src.roteamento import Roteamento


class Simulacao:
    def __init__(self, grafo: GrafoDistancia, caminhões: list):
        self.grafo = grafo
        self.caminhões = caminhões
        self.entregas = []

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)

    def executar_simulacao(self):
        roteamento = Roteamento(self.grafo, self.caminhões)
        for entrega in self.entregas:
            try:
                roteamento.adicionar_entrega(entrega)
            except ValueError as e:
                logging.error(f"Erro ao adicionar entrega: {e}")

        roteamento.alocar_entregas()

    def relatorio(self):
        total_entregas = len(self.entregas)
        entregas_alocadas = sum(1 for entrega in self.entregas if getattr(entrega, 'alocada', False))
        logging.info(f"Total de entregas: {total_entregas}")
        logging.info(f"Entregas alocadas: {entregas_alocadas}")

        # Se desejar, adicione mais detalhes ao relatório
        for entrega in self.entregas:
            if hasattr(entrega, 'alocada') and entrega.alocada:
                logging.info(f"Entrega {entrega.idEntrega} foi alocada.")
            else:
                logging.info(f"Entrega {entrega.idEntrega} não foi alocada.")