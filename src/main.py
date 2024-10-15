import os
from banco_dados import BancoDeDados
from grafo_distancias import GrafoDistancias
from roteamento import Roteamento
from simulacao import Simulacao


def main():
    banco_de_dados = BancoDeDados()

    # Obtendo o diretório atual do script e formando o caminho absoluto
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Definindo o caminho absoluto para os arquivos
    centros_path = os.path.join(base_dir, 'data/centros_distribuicao.csv')
    caminhoes_path = os.path.join(base_dir, 'data/caminhoes.csv')
    entregas_path = os.path.join(base_dir, 'data/entregas.csv')
    grafo_path = os.path.join(base_dir, 'data/distancias.csv')

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


if __name__ == "__main__":
    main()
