from entrega import Entrega

class Caminhao:
    def __init__(self, idCaminhao: int, capacidade: int, horas_operacao_max: int):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.horas_operacao_max = horas_operacao_max
        self.localizacaoAtual = None
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True

    def adicionar_entrega(self, entrega: Entrega):
        self.carga_atual += entrega.quantidade_carga
        self.horas_operacao_atual += self.estimar_tempo_entrega(entrega)
        self.localizacaoAtual = entrega.destino

    def pode_adicionar_entrega(self, entrega: Entrega) -> bool:
        carga_total = self.carga_atual + entrega.quantidade_carga
        horas_total = self.horas_operacao_atual + self.estimar_tempo_entrega(entrega)
        return carga_total <= self.capacidade and horas_total <= self.horas_operacao_max

    def estimar_tempo_entrega(self, entrega: Entrega) -> int:
        return 2

    def esta_disponivel(self) -> bool:
        return self.disponivel and self.horas_operacao_atual < self.horas_operacao_max

    def resetar_dia(self):
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True