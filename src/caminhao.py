class Caminhao:
    def __init__(self, idCaminhao, capacidade, localizacaoAtual):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.localizacaoAtual = localizacaoAtual
        self.cargaAtual = 0
        self.disponivel = True

    def carregarEntrega(self, carga):
        if self.cargaAtual + carga <= self.capacidade:
            self.cargaAtual += carga
            return True
        return False

    def atualizarLocalizacao(self, localizacao):
        self.localizacaoAtual = localizacao

    def isDisponivel(self):
        return self.disponivel

    def finalizarEntrega(self):
        self.cargaAtual = 0
        self.disponivel = True

