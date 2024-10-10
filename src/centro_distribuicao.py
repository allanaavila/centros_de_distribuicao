class CentroDistribuicao:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        self.caminhoes = []

    def adicionarCaminhoes(self, caminhao):
        self.caminhoes.append(caminhao)

    def desparcharCaminhoes(self, entrega):
        for caminhao in self.caminhoes:
            if caminhao.isDisponivel():
               if caminhao.carregarEntrega(entrega.volume):
                   caminhao.atualizarLocalizacao(entrega.destino)
                   caminhao.disponivel = False
                   return caminhao
        return None

    def listarCaminhoes(self):
        return self.caminhoes


