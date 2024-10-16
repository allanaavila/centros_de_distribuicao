import os
from banco_dados import BancoDeDados
from grafo_distancias import GrafoDistancia
from simulacao import Simulacao


def main():
    banco_de_dados = BancoDeDados()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    centros_path = os.path.join(base_dir, '../data/centros_distribuicao.csv')
    caminhoes_path = os.path.join(base_dir, '../data/caminhoes.csv')
    entregas_path = os.path.join(base_dir, '../data/entregas.csv')
    grafo_path = os.path.join(base_dir, '../data/distancias.csv')


    try:
        centros = banco_de_dados.carregar_centros(centros_path)
        print("Centros carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar centros: {e}")
        return

    try:
        caminhões = banco_de_dados.carregar_caminhoes(caminhoes_path)
        print("Caminhões carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar caminhões: {e}")
        return

    try:
        entregas = banco_de_dados.carregar_entregas(entregas_path)
        print("Entregas carregadas com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar entregas: {e}")
        return

    try:
        grafo = banco_de_dados.carregar_grafo_distancias(grafo_path)
        print("Grafo de distâncias carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar grafo de distâncias: {e}")
        return

    try:
        simulacao = Simulacao(banco_de_dados)
        simulacao.executar_simulacao()
        print("Simulação executada com sucesso.")
    except Exception as e:
        print(f"Erro ao executar simulação: {e}")
        return

    try:
        banco_de_dados.salvar_centros(centros_path)
        banco_de_dados.salvar_caminhoes(caminhoes_path)
        banco_de_dados.salvar_entregas(entregas_path)
        banco_de_dados.salvar_grafo_distancias(grafo_path)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


if __name__ == "__main__":
    main()