import csv
from caminhao import Caminhao
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia

class BancoDeDados:
    def __init__(self):
        self.centros = []
        self.entregas = []
        self.distancias = {}
        self.grafo = GrafoDistancia()

    def carregar_centros(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    centro = CentroDistribuicao(row['nome'], row['cidade'], row['estado'])
                    self.centros.append(centro)
                except KeyError as e:
                    print(f"Erro ao carregar centros: coluna faltando {str(e)} no arquivo.")

    def carregar_caminhoes(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    capacidade = int(row['capacidade'])
                    horas_operacao_max = int(row['horas_operacao_max'])
                    caminhao = Caminhao(idCaminhao=int(row['id']), capacidade=capacidade,
                                        horas_operacao_max=horas_operacao_max, grafo=self.grafo)

                    for centro in self.centros:
                        if centro.localizacao == f"{row['cidade']}, {row['estado']}":
                            centro.adicionar_caminhao(caminhao)
                            break
                except KeyError as e:
                    print(f"Erro ao carregar caminhões: coluna faltando {str(e)} no arquivo.")
                except Exception as e:
                    print(f"Erro ao criar caminhão: {e}")

    def carregar_entregas(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    entrega = Entrega(
                        idEntrega=int(row['idEntrega']),
                        centro_nome=row['centro_nome'],
                        destino=row['destino'],
                        quantidade_carga=int(row['quantidade_carga']),
                        prazoEntrega=int(row['prazoEntrega'])
                    )
                    for centro in self.centros:
                        if centro.nome == row['centro_nome']:
                            centro.adicionar_entrega(entrega)
                            break
                except KeyError as e:
                    print(f"Erro ao carregar entregas: coluna faltando {str(e)} no arquivo.")
                except ValueError as e:
                    print(f"Erro ao criar entrega: {e}")


    def carregar_grafo_distancias(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                origem = row['origem']
                destino = row['destino']
                distancia = int(row['distancia'])

                self.grafo.adicionar_vertice(origem)
                self.grafo.adicionar_vertice(destino)
                self.grafo.adicionar_aresta(origem, destino, distancia)
        return self.grafo


    def salvar_centros(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nome', 'localizacao']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for centro in self.centros:
                writer.writerow({'nome': centro.nome, 'localizacao': centro.localizacao})

    def salvar_caminhoes(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'capacidade', 'horas_operacao_max', 'centro_nome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for centro in self.centros:
                for caminhao in centro.caminhoes:
                    writer.writerow({'id': caminhao.idCaminhao,
                                     'capacidade': caminhao.capacidade,
                                     'horas_operacao_max': caminhao.horas_operacao_max,
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
            for origem in self.grafo.vertices:  # Iterate over the graph vertices
                for destino, distancia in self.grafo.distancias[origem].items():
                    writer.writerow({'origem': origem,
                                     'destino': destino,
                                     'distancia': distancia})