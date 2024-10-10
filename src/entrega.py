class Entrega:
    def __init__(self, idEntrega, destino, volume, prazo):
        self.idEntrega = idEntrega
        self.destino = destino
        self.volume = volume
        self.prazo = prazo
        self.status = "Pendente"

    def atualizarStatus(self, status):
        self.status = status


