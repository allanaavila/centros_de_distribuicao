from typing import Dict, List

from bokeh.models import canvas
from reportlab.lib.pagesizes import letter
from centro_distribuicao import CentroDistribuicao
from roteamento import Rota
import matplotlib.pyplot as plt
import os

class Relatorio:
    def __init__(self, dias_simulacao: int, centros: List[CentroDistribuicao]):
        self.dias_simulacao = dias_simulacao
        self.centros = centros
        self.estatisticas_por_dia: Dict[int, Dict] = {}

    def registrar_dia(self, dia: int, rotas_por_centro: Dict[CentroDistribuicao, List[Rota]]):
        estatisticas_dia = {
            'entregas_realizadas': 0,
            'distancia_total': 0,
            'entregas_atrasadas': 0,
            'utilizacao_caminhoes': {}
        }

        for centro, rotas in rotas_por_centro.items():
            for rota in rotas:
                estatisticas_dia['entregas_realizadas'] += len(rota.entregas)
                estatisticas_dia['distancia_total'] += rota.distancia_total
                estatisticas_dia['entregas_atrasadas'] += sum(1 for e in rota.entregas if e.esta_atrasada())

                utilizacao = (rota.caminhao.carga_atual / rota.caminhao.capacidade) * 100
                estatisticas_dia['utilizacao_caminhoes'][rota.caminhao.idCaminhao] = utilizacao

        self.estatisticas_por_dia[dia] = estatisticas_dia

    def gerar_relatorio_final(self, file_path="../docs/relatorio_simulacao.pdf"):
        total_entregas = sum(dia['entregas_realizadas'] for dia in self.estatisticas_por_dia.values())
        total_distancia = sum(dia['distancia_total'] for dia in self.estatisticas_por_dia.values())
        total_atrasos = sum(dia['entregas_atrasadas'] for dia in self.estatisticas_por_dia.values())

        eficiencia = (total_entregas - total_atrasos) / total_entregas * 100 if total_entregas > 0 else 0
        media_utilizacao_caminhoes = self.calcular_media_utilizacao_caminhoes()

        c = canvas.Canvas(file_path, pagesize=letter)
        c.drawString(100, 750, f"Relatório Final Detalhado da Simulação:")
        c.drawString(100, 730, f"Total de dias simulados: {self.dias_simulacao}")
        c.drawString(100, 710, f"Total de entregas realizadas: {total_entregas}")
        c.drawString(100, 690, f"Distância total percorrida: {total_distancia:.2f} km")
        c.drawString(100, 670, f"Número total de entregas atrasadas: {total_atrasos}")
        c.drawString(100, 650, f"Eficiência geral do sistema: {eficiencia:.2f}%")
        c.drawString(100, 630, f"Utilização média dos caminhões: {media_utilizacao_caminhoes:.2f}%")

        self.gerar_grafico_entregas_por_dia(file_path)

        c.showPage()
        c.drawImage("grafico_entregas_por_dia.png", 100, 400, width=400, height=300)
        c.save()

        os.remove("./temp/grafico_entregas_por_dia.png")

    def calcular_media_utilizacao_caminhoes(self) -> float:
        total_utilizacao = 0
        total_caminhoes = 0
        for dia in self.estatisticas_por_dia.values():
            total_utilizacao += sum(dia['utilizacao_caminhoes'].values())
            total_caminhoes += len(dia['utilizacao_caminhoes'])
        return total_utilizacao / total_caminhoes if total_caminhoes > 0 else 0

    def gerar_grafico_entregas_por_dia(self, file_path: str):
        dias = list(self.estatisticas_por_dia.keys())
        entregas = [dia['entregas_realizadas'] for dia in self.estatisticas_por_dia.values()]

        plt.figure(figsize=(10, 6))
        plt.plot(dias, entregas, marker='o', linestyle='-', color='b', label='Entregas por Dia')

        plt.title('Entregas Realizadas por Dia')
        plt.xlabel('Dia')
        plt.ylabel('Número de Entregas')
        plt.grid(True)

        plt.legend()

        plt.savefig("./temp/grafico_entregas_por_dia.png")
        plt.close()