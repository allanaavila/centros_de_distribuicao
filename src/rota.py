from src.caminhao import Caminhao
from src.entrega import Entrega
from typing import List, Dict

class Rota:
    def __init__(self, caminhao: Caminhao):
        self.caminhao = caminhao
        self.entregas: List[Entrega] = []
        self.distancia_total = 0

    def adicionar_entrega(self, entrega: Entrega, distancia: int):
        self.entregas.append(entrega)
        self.distancia_total += distancia