import os
import csv
import heapq
from banco_dados import BancoDeDados
from grafo_distancias import GrafoDistancia
from roteamento import Roteamento
from simulacao import Simulacao
from relatorios import Relatorio

def main():
    banco_de_dados = BancoDeDados()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    centros_path = os.path.join(base_dir, '../data/centros_distribuicao.csv')
    caminhoes_path = os.path.join(base_dir, '../data/caminhoes.csv')
    entregas_path = os.path.join(base_dir, '../data/entregas.csv')
    grafo_path = os.path.join(base_dir, '../data/distancias.csv')

    if not os.path.isfile(centros_path):
        print(f"Erro: O arquivo {centros_path} não foi encontrado.")
        return

    centros = banco_de_dados.carregar_centros(centros_path)

    if not os.path.isfile(caminhoes_path):
        print(f"Erro: O arquivo {caminhoes_path} não foi encontrado.")
        return

    banco_de_dados.carregar_caminhoes(caminhoes_path)

    if not os.path.isfile(entregas_path):
        print(f"Erro: O arquivo {entregas_path} não foi encontrado.")
        return

    banco_de_dados.carregar_entregas(entregas_path)

    if not os.path.isfile(grafo_path):
        print(f"Erro: O arquivo {grafo_path} não foi encontrado.")
        return

    grafo = banco_de_dados.carregar_grafo_distancias(grafo_path)

    simulacao = Simulacao(banco_de_dados)
    simulacao.executar_simulacao()

    banco_de_dados.salvar_centros(centros_path)
    banco_de_dados.salvar_caminhoes(caminhoes_path)
    banco_de_dados.salvar_entregas(entregas_path)
    banco_de_dados.salvar_grafo_distancias(grafo_path)


if __name__ == "_main_":
    main()