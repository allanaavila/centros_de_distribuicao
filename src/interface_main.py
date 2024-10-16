import os
from banco_dados import BancoDeDados
from grafo_distancias import GrafoDistancia
from simulacao import Simulacao


class InterfaceTerminal:
    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    def exibir_menu(self):
        while True:
            print("--- Menu Principal ---")
            print("1. Carregar dados")
            print("2. Executar simulação")
            print("3. Salvar dados")
            print("4. Sair")

            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                self.carregar_dados()
            elif escolha == '2':
                self.executar_simulacao()
            elif escolha == '3':
                self.salvar_dados()
            elif escolha == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def carregar_dados(self):
        try:
            self.banco_de_dados.carregar_centros('../data/centros_distribuicao.csv')
            self.banco_de_dados.carregar_caminhoes('../data/caminhoes.csv')
            self.banco_de_dados.carregar_entregas('../data/entregas.csv')
            self.banco_de_dados.carregar_grafo_distancias('../data/distancias.csv')
            print("Dados carregados com sucesso!")
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
            self.banco_de_dados.salvar_centros('centros_salvos.csv')
            self.banco_de_dados.salvar_caminhoes('caminhoes_salvos.csv')
            self.banco_de_dados.salvar_entregas('entregas_salvas.csv')
            self.banco_de_dados.salvar_grafo_distancias('distancias_salvas.csv')
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
