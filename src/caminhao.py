from src.entrega import Entrega
from src.grafo_distancias import GrafoDistancia


class Caminhao:
    def __init__(self, idCaminhao: int, capacidade: int, horas_operacao_max: int, grafo: GrafoDistancia):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.horas_operacao_max = horas_operacao_max
        self.localizacaoAtual = None
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True
        self.grafo = grafo

    def adicionar_entrega(self, entrega: Entrega):
        if self.pode_adicionar_entrega(entrega):
            self.carga_atual += entrega.quantidade_carga
            tempo_entrega = self.estimar_tempo_entrega(entrega)
            self.horas_operacao_atual += tempo_entrega
            self.localizacaoAtual = entrega.destino
        else:
            print("Não é possível adicionar a entrega: carga ou tempo de operação excedido.")

    def pode_adicionar_entrega(self, entrega: Entrega) -> bool:
        carga_total = self.carga_atual + entrega.quantidade_carga
        horas_total = self.horas_operacao_atual + self.estimar_tempo_entrega(entrega)
        return carga_total <= self.capacidade and horas_total <= self.horas_operacao_max

    def estimar_tempo_entrega(self, entrega: Entrega) -> int:
        if self.localizacaoAtual:
            distancia = self.grafo.obter_distancia(self.localizacaoAtual, entrega.destino)
            if distancia is not None:
                return distancia / 50
            else:
                print("Distância não encontrada entre as localizações.")
                return float('inf')
        return 2

    def esta_disponivel(self) -> bool:
        return self.disponivel and self.horas_operacao_atual < self.horas_operacao_max

    def resetar_dia(self):
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True