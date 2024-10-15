import csv
from src.caminhao import Caminhao
from src.centro_distribuicao import CentroDistribuicao
from src.entrega import Entrega
from src.grafo_distancias import GrafoDistancias

class BancoDeDados:
    def __init__(self):
        self.centros = []
        self.entregas = []
        self.distancias = {}

    def carregar_centros(self, filename):
        centros = []
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                centro = CentroDistribuicao(row['nome'], row['localizacao'])
                centros.append(centro)
        self.centros = centros  # Armazenar centros na instância
        return centros

    def carregar_caminhoes(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                caminhao = Caminhao(int(row['capacidade_maxima']), int(row['horas_operacao']))
                for centro in self.centros:
                    if centro.cidade == row['centro_nome']:  # Usar o atributo correto
                        centro.adicionar_caminhao(caminhao)
                        break

    def carregar_entregas(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entrega = Entrega(row['destino'], int(row['quantidade_carga']), int(row['prazo']))
                for centro in self.centros:
                    if centro.cidade == row['centro_nome']:  # Usar o atributo correto
                        centro.adicionar_entrega(entrega)
                        break

    def carregar_grafo_distancias(self, filename):
        grafo = GrafoDistancias()
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Adiciona as arestas (distâncias) entre os vértices
                grafo.adicionar_distancia(row['origem'], row['destino'], float(row['distancia']))
        return grafo
