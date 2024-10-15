class Entrega:
    def __init__(self, idEntrega, origem, destino, peso, prazoEntrega):
        self.idEntrega = idEntrega
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.prazoEntrega = prazoEntrega
        self.caminhao_associado = None

    def associar_caminhao(self, caminhao):
        self.caminhao_associado = caminhao
        print(f"Caminhão {caminhao.idCaminhao} associado à entrega {self.idEntrega}.")

    def __str__(self):
        return (f"Entrega {self.idEntrega} - "
                f"Origem: {self.origem} - "
                f"Destino: {self.destino} - "
                f"Peso: {self.peso} kg - "
                f"Prazo de Entrega: {self.prazoEntrega} - "
                f"Caminhão Associado: {self.caminhao_associado.idCaminhao if self.caminhao_associado else 'Nenhum'}")