class Entrega:
    def __init__(self, destino, volume, prazo):
        self.destino = destino
        self.volume = volume
        self.prazo = prazo
        self.status = "Pendente"

    def atualizar_status(self, novo_status):
        self.status = novo_status
        
    def __str__(self):
        return f"Entrega(destino={self.destino}, volume={self.volume}, prazo={self.prazo}, status={self.status})"
