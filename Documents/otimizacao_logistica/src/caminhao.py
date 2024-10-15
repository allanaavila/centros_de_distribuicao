class Caminhao:
    def __init__(self, idCaminhao, capacidade, localizacaoAtual):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.localizacaoAtual = localizacaoAtual
        self.disponivel = True

    def realizar_entrega(self, entrega):
        if self.disponivel:
            print(f"Caminhão {self.idCaminhao} realizando entrega: {entrega}")
            self.localizacaoAtual = entrega['destino']
            self.disponivel = False
        else:
            print(f"Caminhão {self.idCaminhao} não está disponível para entrega.")

    def finalizar_entrega(self):
        self.disponivel = True
        print(f"Caminhão {self.idCaminhao} está agora disponível.")

    def verificar_disponibilidade(self):
        return self.disponivel

    def __str__(self):
        return (f"Caminhão {self.idCaminhao} - "
                f"Capacidade: {self.capacidade} toneladas - "
                f"Localização Atual: {self.localizacaoAtual} - "
                f"Disponível: {'Sim' if self.disponivel else 'Não'}")
