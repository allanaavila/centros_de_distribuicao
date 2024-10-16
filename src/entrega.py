class Entrega:
    def __init__(self, idEntrega, centro_nome, destino, quantidade_carga , prazoEntrega):
        if quantidade_carga <= 0:
            raise ValueError("O peso da entrega deve ser maior que zero.")
        if not centro_nome or not destino:
            raise ValueError("Origem e destino não podem ser vazios.")
        if prazoEntrega <= 0:
            raise ValueError("O prazo de entrega deve ser um valor positivo.")

        self.idEntrega = idEntrega
        self.origem = centro_nome
        self.destino = destino
        self.quantidade_carga  = quantidade_carga
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
                f"Quantidade de Carga: {self.quantidade_carga} kg - Prazo de Entrega: {self.prazoEntrega} dias - "
                f"Caminhão Associado: {self.caminhao_associado.idCaminhao if self.caminhao_associado else 'Nenhum'}")