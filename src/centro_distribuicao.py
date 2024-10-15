class CentroDistribuicao:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        self.caminhoes = []

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def despachar_caminhao(self, entrega):
        for caminhao in self.caminhoes:
            if caminhao.disponivel():
                caminhao.realizar_entrega(entrega)
                return caminhao
        return None

    def adicionar_entrega(self, entrega):
        print(f"Adicionando entrega: {entrega}")
        caminhão_despachado = self.despachar_caminhao(entrega)
        if caminhão_despachado:
            print(f"Caminhão {caminhão_despachado.id} despachado para a entrega.")
        else:
            print("Nenhum caminhão disponível para despachar.")

    def __str__(self):
        return f"{self.cidade} - {self.estado}"