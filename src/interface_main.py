import os
from banco_dados import BancoDeDados
from grafo_distancias import GrafoDistancia
from simulacao import Simulacao


class InterfaceTerminal:
    def __init__(self):
        banco_de_dados = BancoDeDados()
        base_dir = os.path.dirname(os.path.abspath(__file__))

        centros_path = os.path.join(base_dir, '../data/centros_distribuicao.csv')
        caminhoes_path = os.path.join(base_dir, '../data/caminhoes.csv')
        entregas_path = os.path.join(base_dir, '../data/entregas.csv')
        grafo_path = os.path.join(base_dir, '../data/distancias.csv')

    def carregar_dados(self):
        try:
            self.banco_de_dados.carregar_centros(self.centros_path)
            print("Centros carregados com sucesso.")
            self.banco_de_dados.carregar_caminhoes(self.caminhoes_path)
            print("Caminhões carregados com sucesso.")
            self.banco_de_dados.carregar_entregas(self.entregas_path)
            print("Entregas carregadas com sucesso.")
            self.banco_de_dados.carregar_grafo_distancias(self.grafo_path)
            print("Grafo de distâncias carregado com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")


    def executar_simulacao(self):
        try:
            simulacao = Simulacao(self.banco_de_dados)
            simulacao.executar_simulacao()
            print("Simulação executada com sucesso.")
        except Exception as e:
            print(f"Erro ao executar simulação: {e}")

    def salvar_dados(self):
        try:
            self.banco_de_dados.salvar_centros(self.centros_path)
            self.banco_de_dados.salvar_caminhoes(self.caminhoes_path)
            self.banco_de_dados.salvar_entregas(self.entregas_path)
            self.banco_de_dados.salvar_grafo_distancias(self.grafo_path)
            print("Dados salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def exibir_menu(self):
        while True:
            print("\n--- Menu Principal ---")
            print("1. Carregar dados")
            print("2. Executar simulação")
            print("3. Salvar dados")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.carregar_dados()
            elif opcao == '2':
                self.executar_simulacao()
            elif opcao == '3':
                self.salvar_dados()
            elif opcao == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")