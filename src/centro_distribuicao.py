class CentroDistribuicao:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        self.caminhoes = []  # Lista de caminhões disponíveis

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def despachar_caminhao(self, entrega):
        # Lógica para despachar um caminhão, verificando disponibilidade
        for caminhao in self.caminhoes:
            if caminhao.disponivel():
                return caminhao
        return None
    
    def adicionar_entrega(self, entrega):
        print(entrega)