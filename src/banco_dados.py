class BancoDeDados:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BancoDeDados, cls).__new__(cls)
            cls.centro_distribuicao = []
            cls.caminhao = []
            cls.entregas = []
        return cls._instance

    def adicionarCentroDistribuicao(self, centro_distribuicao):
        self.centro_distribuicao.append(centro_distribuicao)

    def adicionarCaminho(self, caminho):
        self.caminhao.append(caminho)

    def adicionarEntrega(self, entrega):
        self.entregas.append(entrega)

    def obterCentrosMaisProximos(self, lat, lon):
        pass

    def listarCaminhoesDisponiveis(self):
        return [c for c in self.caminhao if c.disponivel()]


