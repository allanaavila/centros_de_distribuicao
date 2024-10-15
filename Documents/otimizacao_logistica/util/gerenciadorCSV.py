# src/util/gerenciador_csv.py

import os
import pandas as pd


class GerenciadorCSV:
    def __init__(self, caminho_relativo, caminho_absoluto):
        self.caminho_relativo = caminho_relativo
        self.caminho_absoluto = caminho_absoluto
        print(
            f"Inicializando GerenciadorCSV com caminho_relativo: {caminho_relativo} e caminho_absoluto: {caminho_absoluto}")

    def verificar_existencia_arquivo(self):
        print(f"Verificando os caminhos: {self.caminho_absoluto} e {self.caminho_relativo}")
        if os.path.exists(self.caminho_absoluto):
            print("Arquivo encontrado no caminho absoluto.")
            return self.caminho_absoluto
        elif os.path.exists(self.caminho_relativo):
            print("Arquivo encontrado no caminho relativo.")
            return self.caminho_relativo
        else:
            print("Arquivo não foi encontrado em nenhum caminho.")
            print(f"Verifiquei os caminhos: {self.caminho_absoluto} e {self.caminho_relativo}")
            return None

    def ler_csv(self):
        caminho = self.verificar_existencia_arquivo()
        if caminho:
            df = pd.read_csv(caminho)
            return df
        else:
            return None
