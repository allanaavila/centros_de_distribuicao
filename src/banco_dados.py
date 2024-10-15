import csv
from caminhao import Caminhao
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia

class BancoDeDados:
    def _init_(self):
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
        self.centros = centros
        return centros

    def carregar_caminhoes(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                caminhao = Caminhao(int(row['capacidade_maxima']), int(row['horas_operacao']), row['centro_nome'])
                for centro in self.centros:
                    if centro.nome == row['centro_nome']:
                        centro.adicionar_caminhao(caminhao)
                        break


    def carregar_entregas(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entrega = Entrega(row['destino'], int(row['quantidade_carga']), int(row['prazo']))
                for centro in self.centros:
                    if centro.nome == row['centro_nome']:  # Verifique se o atributo é 'nome'
                        centro.adicionar_entrega(entrega)
                        break

    def carregar_grafo_distancias(self, filename):
        grafo = GrafoDistancia()
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                grafo.adicionar_distancia(row['origem'], row['destino'], float(row['distancia']))
        return grafo

    def salvar_centros(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nome', 'localizacao']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for centro in self.centros:
                writer.writerow(
                    {'nome': centro.nome, 'localizacao': centro.localizacao})

    def salvar_caminhoes(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['capacidade_maxima', 'horas_operacao', 'centro_nome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for centro in self.centros:
                for caminhao in centro.caminhoes:
                    writer.writerow({'capacidade_maxima': caminhao.capacidade,
                                     'horas_operacao': caminhao.horas_operacao,
                                     'centro_nome': centro.nome})

    def salvar_entregas(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['destino', 'quantidade_carga', 'prazo', 'centro_nome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for centro in self.centros:
                for entrega in centro.entregas:
                    writer.writerow({'destino': entrega.destino,
                                     'quantidade_carga': entrega.quantidade_carga,
                                     'prazo': entrega.prazo,
                                     'centro_nome': centro.nome})

    def salvar_grafo_distancias(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['origem', 'destino', 'distancia']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for origem, destinos in self.distancias.items():
                for destino, distancia in destinos.items():
                    writer.writerow({'origem': origem,
                                     'destino': destino,
                                     'distancia': distancia})