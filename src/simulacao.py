import logging
from typing import List, Dict
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia
from roteamento import Roteamento


class Simulacao:
    def __init__(self, grafo: GrafoDistancia, centros: List[CentroDistribuicao], dias_simulacao: int):
        self.grafo = grafo
        self.centros = centros
        self.dias_simulacao = dias_simulacao
        self.entregas_por_dia: Dict[int, List[Entrega]] = {}
        self.estatisticas = {
            'entregas_realizadas': 0,
            'distancia_total': 0,
            'entregas_atrasadas': 0
        }

    def adicionar_entrega(self, entrega: Entrega, dia: int):
        if dia not in self.entregas_por_dia:
            self.entregas_por_dia[dia] = []
        self.entregas_por_dia[dia].append(entrega)

    def executar_simulacao(self):
        for dia in range(1, self.dias_simulacao + 1):
            logging.info(f"Iniciando simulação do dia {dia}")
            self.simular_dia(dia)
        self.gerar_relatorio_final()

    def simular_dia(self, dia: int):
        entregas_do_dia = self.entregas_por_dia.get(dia, [])
        roteamento = Roteamento(self.grafo, self.centros)

        for entrega in entregas_do_dia:
            centro_mais_proximo = roteamento.encontrar_centro_mais_proximo(entrega.destino)
            roteamento.adicionar_entrega(entrega, centro_mais_proximo)

        rotas_otimizadas = roteamento.alocar_entregas()

        for centro, rotas in rotas_otimizadas.items():
            for rota in rotas:
                self.estatisticas['entregas_realizadas'] += len(rota.entregas)
                self.estatisticas['distancia_total'] += rota.distancia_total
                self.estatisticas['entregas_atrasadas'] += sum(1 for e in rota.entregas if e.esta_atrasada())

    def gerar_relatorio_final(self):
        logging.info("Relatório Final da Simulação:")
        logging.info(f"Total de dias simulados: {self.dias_simulacao}")
        logging.info(f"Total de entregas realizadas: {self.estatisticas['entregas_realizadas']}")
        logging.info(f"Distância total percorrida: {self.estatisticas['distancia_total']} km")
        logging.info(f"Número de entregas atrasadas: {self.estatisticas['entregas_atrasadas']}")
        eficiencia = (self.estatisticas['entregas_realizadas'] - self.estatisticas['entregas_atrasadas']) / \
                     self.estatisticas['entregas_realizadas'] * 100
        logging.info(f"Eficiência do sistema: {eficiencia:.2f}%")