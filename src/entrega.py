class Entrega:
    def __init__(self, idEntrega, origem, destino, peso, prazoEntrega):
        if peso <= 0:
            raise ValueError("O peso da entrega deve ser maior que zero.")
        if not origem or not destino:
            raise ValueError("Origem e destino não podem ser vazios.")
        if prazoEntrega <= 0:
            raise ValueError("O prazo de entrega deve ser um valor positivo.")

        self.idEntrega = idEntrega
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.prazoEntrega = prazoEntrega
        self.caminhao_associado = None

    def associar_caminhao(self, caminhao):
        if caminhao is None:
            raise ValueError("O caminhão não pode ser nulo.")
        if not caminhao.esta_disponivel():
            raise ValueError(f"O Caminhão {caminhao.idCaminhao} não está disponível.")
        self.caminhao_associado = caminhao
        caminhao.adicionar_entrega(self)
        print(f"Caminhão {caminhao.idCaminhao} associado à entrega {self.idEntrega}.")

    def __str__(self):
        return (f"Entrega {self.idEntrega} - Origem: {self.origem} - Destino: {self.destino} - "
                f"Peso: {self.peso} kg - Prazo de Entrega: {self.prazoEntrega} dias - "
                f"Caminhão Associado: {self.caminhao_associado.idCaminhao if self.caminhao_associado else 'Nenhum'}")