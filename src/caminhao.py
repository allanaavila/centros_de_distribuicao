class Caminhao:
    def __init__(self, idCaminhao, capacidade, localizacaoAtual):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.localizacaoAtual = localizacaoAtual
        self.disponivel = True  # Status de disponibilidade

    def finalizar_entrega(self):
        self.disponivel = True  # Marca como disponível após a entrega
